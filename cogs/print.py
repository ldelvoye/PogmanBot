# Print function that provides an embedded text box of dimensions <d>
import discord
from discord.ext import commands

def embed(CourseName, Date, Colour, CalendarLink, NumDeadlines):
    # {CourseName, Date, Colour, CalendarLink} = String --- NumDeadlines = Int.
    embed = discord.Embed(
        Title = Date,
        colour = Colour  
    )
    embed.set_footer(text = CalendarLink)
    embed.set_author(text = CourseName)
    # Loop to create field per upcoming deadline (max 3)
       # embed.add_field(name = >>AssignmentName<<, value = >>AssignmentDueDate<<, inline = False)
       # {AssignmentName, AssignmentDueDate} = String
    
    return embed