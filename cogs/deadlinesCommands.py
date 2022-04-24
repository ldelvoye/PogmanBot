# Deadlines by class & coop --> list
    # @PogmanBot ECE140
    # @PogmanBot coop
# General deadlines --> list
    # @PogmanBot

import discord
from discord.ext import commands
from prettytable import PrettyTable
import cogs.db_funcs as func


class deadlinesCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def course(self, ctx, course):
        table = PrettyTable()
        
            
    @commands.command()
    async def coopapp(self, ctx):
        table = PrettyTable()
        table.field_names = func.retrieve_column_headers(f"{course}")[:5]
        deadlines = func.get_specific_course_values(f"{course}")
        for i in range(len(deadlines)): 
            table.add_row(deadlines[i][:5])

        await ctx.channel.send(f"```\n{table}\n```")
        
        
    @commands.command()
    async def coopmatch(self, ctx):
        table = PrettyTable()
        columns = func.retrieve_column_headers(f"{course}")
        deadlines = func.get_specific_course_values(f"{course}")

        actual_columns = []
        actual_deadlines = []
        for i in range(len(columns)):
            if i not in [1,2,3,4]:
                actual_columns.append(columns[i])
        table.field_names = actual_columns
        
        for i in range(len(deadlines)):
            actual_deadlines.append([])
            for j in range(len(deadlines[i])):
                if j not in [1,2,3,4]:
                    actual_deadlines[i].append(deadlines[i][j])

        for i in range(len(deadlines)): 
            table.add_row(actual_deadlines[i])


        await ctx.channel.send(f"```\n{table}\n```")
        
        
        
def setup(bot):
    bot.add_cog(deadlinesCommands(bot))