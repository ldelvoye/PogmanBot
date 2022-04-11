import discord
from discord.ext import commands
from config import TOKEN

extensions = ['cogs.help_commands',
              'cogs.deadlines_commands',
              'cogs.reminder_commands']

bot = commands.Bot(command_prefix='@PogmanBot')

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extensions(ext)
        
@bot.event
async def on_ready():
    print('Bot is ready.')

bot.run(TOKEN)
