# Every 24 hours, <@Daily Reminders> with upcoming 48 hour deadlines
# Coop rankings, <@Daily Reminders>
# 24 hours before general coop application deadlines, <@Daily Reminders>

import discord
from discord.ext import commands

class reminderCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
def setup(bot):
    bot.add_cog(reminderCommands(bot))