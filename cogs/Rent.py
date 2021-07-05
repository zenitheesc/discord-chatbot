import pymongo
from discord.ext import tasks, commands
from util import *
from config import MONGODB_ATLAS_URI
from config import CHANNEL_ID

from time import time

class Rent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.time_expired.start()

        client = pymongo.MongoClient(MONGODB_ATLAS_URI)
        self.db = client['discord-bot']['discord-bot']
        self.id = self.db.find_one({"description": "rent"})['rent']['discord_id']
        self.time = self.db.find_one({"description": "rent"})['rent']['rent_time']

    #A function to register the rent of a beaglebone black for 2 hours
    @commands.command(
        brief='Uma função para alugar a Beaglebone Black de Maíra Canal (gerente do Alto Nível)',
        help='Use o comando >alugar para ter acesso irrestrito durante duas horas a uma Beaglebone Black. Caso alguém já esteja de posse dela, você será avisado/avisada',
        aliases=['aluguel','aluga','alugar']
    )
    async def alugar(self, ctx):
        await ctx.trigger_typing()

        print(f'\n [*] \'>alugar\' command called.')

        await reactToMessage(self.bot, ctx.message, [MESSAGE_EMOJI])

        if not self.db.find_one({"description": "rent"}) or self.id == 0:
            self.db.update_one({"description": "rent"}, {"$set":{"discord_id": ctx.message.author.id}}, upsert=True)
            self.db.update_one({"description": "rent"}, {"$set":{"rent_time": time()/3600}}, upsert = True)
            response = await ctx.send(f'A Beaglebone foi alugada com sucesso por `{ctx.author.mention}`, por duas horas a Beaglebone Black estará sobre sua posse')
        else:
            response = await ctx.send(f'A Beaglebone já foi alugada por <@`{self.id}`>, entre em contato com ela/ele ou aguarde o tempo de devolução')

        await reactToResponse(self.bot, response, [MESSAGE_EMOJI])

    #A function to return the beaglebone black before 2 hours of usage
    @commands.command(
        brief='Uma função para devolver a beagleboneblack caso ja tenha sido alugada',
        help='Use o comando devolver só quando estiver empossado/empossada da Beaglebone Black a fim de devolver ela para o grupo',
        aliases=['devolução','desalugar','desaluga']
    )
    async def devolver(self, ctx):
        await ctx.trigger_typing()

        print(f'\n [*] \'>devolver\' command called.')

        await reactToMessage(self.bot, ctx.message, [MESSAGE_EMOJI])

        if ctx.message.author.id != self.id:
            response = await ctx.send(f'Você não está de posse da Beaglebone. Alugue usando `>alugar` caso ela esteja livre.')
        else:
            self.db.update_one({"description": "rent"}, {"$set":{"discord_id": 0}})
            response = await ctx.send(f'A Beaglebone foi devolvida. Obrigado `{ctx.author.mention}`!')

        await reactToResponse(self.bot, response, [MESSAGE_EMOJI])


    @tasks.loop(minutes = 10)
    async def time_expired(self):
        if time()/3600 - self.time >= 2:
            if self.id != 0:
                txt = (f'O tempo de uso da beaglebone expirou <@`{self.id}`>. Alugue-a novamente caso não existam solicitações de aluguel anteriores.')
                channel = await self.bot.fetch_channel(CHANNEL_ID)
                await channel.send(content=txt)
                self.db.update({"description": "rent"}, {"$set":{"discord_id": 0}})

def setup(bot):
    bot.add_cog(Rent(bot))

