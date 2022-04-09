import discord
from config import TOKEN



client = discord.Client()

@client.event
async def message(message):
    # recognizes message was sent, grabs username, channel, command string, date
    # interpretation
    # message box
    # printing the message
    return

client.run(TOKEN)
