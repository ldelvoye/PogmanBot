import discord
from discord.ext import commands
from cogs.config import TOKEN
from cogs import db_funcs, setup_db

extensions = ['cogs.helpCommands',
              'cogs.deadlinesCommands',
              'cogs.reminderCommands']

bot = commands.Bot(command_prefix="@")

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)
        
bot.run(TOKEN)
