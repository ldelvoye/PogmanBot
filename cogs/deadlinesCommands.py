# Deadlines by class & coop --> list
    # @PogmanBot ECE140
    # @PogmanBot coop
# General deadlines --> list
    # @PogmanBot

import discord
from discord.ext import commands
from prettytable import PrettyTable
from datetime import datetime
import cogs.db_funcs as func


class deadlinesCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    def formatting_embed(self):
        em = discord.Embed(
            title = f"**Upcoming Deadlines**: {datetime.now().date()}"
        )
        
        em.description = f"**-----------------------------------------------------------** \n **Format of Deadlines**: *assignment name* - *due date* -  *worth* \n **-----------------------------------------------------------**"
        
        return em
                
    
    @commands.command()
    async def course(self, ctx, course):
        
        if course == "all":
            em = self.formatting_embed()
            
            specific_values = {}
            values = func.get_specific_course_values(course)
            
            for i in range(len(values)):
                specific_values[i] = {}
                specific_values[i]['assignment_name'] = values[i][0]
                specific_values[i]['due_date'] = values[i][1]
                specific_values[i]['worth'] = values[i][2]
                specific_values[i]['tag'] = values[i][3]
            
            
            for i in range(len(specific_values)):
                em.add_field(
                    name = f"{specific_values[i]['tag']}",
                    value = f"{specific_values[i]['assignment_name']} - {specific_values[i]['due_date']} - {specific_values[i]['worth']}" 
                )
            
        else:
            em = self.formatting_embed()
            
            specific_values = {}
            values = func.get_specific_course_values(course)
            
            for i in range(len(values)):
                specific_values[i] = {}
                specific_values[i]['assignment_name'] = values[i][0]
                specific_values[i]['due_date'] = values[i][1]
                specific_values[i]['worth'] = values[i][2]
                specific_values[i]['tag'] = values[i][3]
            
            
            for i in range(len(specific_values)):
                em.add_field(
                    name = f"{specific_values[i]['tag']}",
                    value = f"{specific_values[i]['assignment_name']} - {specific_values[i]['due_date']} - {specific_values[i]['worth']}" 
                )
            
        
        await ctx.channel.send(embed=em)
        
    @commands.command()
    async def coopapp(self, ctx):
        table = PrettyTable()
        table.field_names = func.retrieve_column_headers(f"1b_coop")[:5]
        deadlines = func.get_coop_values()

        for i in range(len(deadlines)): 
            table.add_row(deadlines[i][:5])

        await ctx.channel.send(f"```\n{table}\n```")
        
        
    @commands.command()
    async def coopmatch(self, ctx):
        table = PrettyTable()
        columns = func.retrieve_column_headers(f"1b_coop")
        deadlines = func.get_coop_values()

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