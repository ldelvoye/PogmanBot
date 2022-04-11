# Deadlines by class & coop --> list
    # @PogmanBot ECE140
    # @PogmanBot coop
# General deadlines --> list
    # @PogmanBot

from print import *
import discord
from discord.ext import commands
import mysql.connector

class deadlinesCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def general_deadlines(self, ctx):
        future_deadlines = 'To be Done (MYSQL)'
        embd = embedMessage(future_deadlines)
        await ctx.channel.send(ctx.message.author.mention + embd)
        
def setup(bot):
    bot.add_cog(deadlinesCommands(bot))