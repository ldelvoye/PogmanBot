# Help command when error command or help command
    # @PogmanBot <anything that isn't a command>
    # @PogmanBot bruh
    # @Pogmanbot help
    
import print
import discord
from discord.ext import commands

class helpCommands(commands.cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(helpCommands(bot))