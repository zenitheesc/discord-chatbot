from discord.ext import tasks, commands
from util import *

import pymongo
from config import MONGODB_ATLAS_URI
from config import CHANNEL_ID

import time

class Rent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.time_expired.start()

        client = pymongo.MongoClient(MONGODB_ATLAS_URI)
        self.db = client['discord-bot']['discord-bot']
        self.rent = self.db.find_one({"description": "rent"})['rent']
        self.time = self.db.find_one({"description": "rent"})['rent_time']

    #A function to register the rent of a beaglebone black for 2 hours
    @commands.command(
        brief='Uma função para alugar a Beaglebone Black de Maíra Canal (gerente do alto nível)',
        help='Use o comando >alugar para ter acesso irrestrito durante duas horas a uma Beaglebone Black. Caso alguém já esteja de posse dela, você será avisado/avisada',
        aliases=['aluguel','beaglebone','aluga'])
    async def alugar(self, ctx):
        await ctx.trigger_typing()

        print(f'\n [*] \'>alugar\' command called.')

        if not self.db.find_one({"description": "rent"})['rent']:
            self.db.update({"description": "rent"},{"$set":{"rent": ctx.message.author.id}})
            self.db.update({"description": "rent"},{"$set":{"rent_time": time.time()/3600}})
            await ctx.send(f'A Beaglebone foi alugada com sucesso por `{ctx.author.mention}`, por duas horas a Beaglebone Black estará sobre sua posse')
        else:
            await ctx.send(f'A Beaglebone já foi alugada por <@`{self.rent}`>, entre em contato com ela/ele ou aguarde o tempo de devolução')
        await reactToMessage(self.bot, ctx.message, [MESSAGE_EMOJI])

    #A function to return the beaglebone black before 2 hours of usage
    @commands.command(
        brief='Uma função para devolver a beagleboneblack caso ja tenha sido alugada',
        help='Use o comando devolver só quando estiver empossado/empossada da Beaglebone Black a fim de devolver ela para o grupo',
        aliases=['devolução','desalugar','desaluga','aluga','beaglebone'])
    async def devolver(self, ctx):
        await ctx.trigger_typing()

        print(f'\n [*] \'>devolver\' command called.')

        if ctx.message.author.id != self.rent:
            await ctx.send(f'Você não está de posse da beaglebone, alugue usando `>alugar` caso ela esteja livre')
        else:
            self.db.update({"description": "rent"}, {"$set":{"rent": None}})
            await ctx.send(f'A beaglebone foi devolvida, obrigado `{ctx.author.mention}`')
        await reactToMessage(self.bot, ctx.message, [MESSAGE_EMOJI])


    @tasks.loop(minutes = 10)
    async def time_expired(self):
        if time.time()/3600 - self.time >= 2:
            txt = (f'O tempo de uso da beaglebone expirou <@`{self.rent}`>. Alugue-a novamente caso não existam solicitações de aluguel anteriores.')
            channel = await self.bot.fetch_channel(CHANNEL_ID)
            await channel.send(context=txt)
            self.db.update({"description": "rent"}, {"$set":{"rent": None}})

def setup(bot):
    bot.add_cog(Rent(bot))

