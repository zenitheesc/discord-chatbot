import discord
from discord.ext import commands
from discord.utils import get
from util import *

import pymongo
from config import MONGODB_ATLAS_URI

import time

class Rent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.time_expired.start()
        
        client = pymongo.MongoClient(MONGODB_ATLAS_URI)
        self.db = client['dicord-bot']['discord-bot']
        self.rent = self.db.find_one({"description": "rent"})['rent']
        self.time = self.db.find_one({"description": "rent"})['rent_time']

    @commands.command()
    async def alugar(self, ctx):
        await ctx.trigger_typing()

        print(f '\n \'>alugar\' command called.')

        if not db.find_one({"description": "rent"})['rent']:
            self.db.update({"description": "rent"},{"$set":{"rent": ctx.message.author}})
            self.db.update({"description": "rent"},{"$set":{"rent_time": time.time()/3600}})
            await ctx.send(f'A beaglebone foi alugada com sucesso por `{ctx.message.author}`, por doze horas a beaglebone estará sobre sua posse')
        else:
            await ctx.send(f'A beaglebone já foi alugada por `{self.rent}`, entre em contato com ela/ele ou aguarde o tempo de devolução')

    @commands.command()
    async def devolver(self, ctx):
        await ctx.trigger_typing()

        print(f '\n \'>devolver\' command called.')

        if ctx.message.author != self.rent:
            await ctx.send(f'Você não está de posse da beaglebone, alugue usando o comando >alugar')
        else:
            self.db.update({"description": "rent"}, {"$set":{"rent": None}})

    @tasks.loop(seconds=100)
    async def time_expired(self):
        if time.time()/3600 - self.time >= 12:
            self.db.update({"description": "rent"}, {"$set":{"rent": None}})


def setup(bot):
    bot.add_cog(Rent(bot))
    


         
