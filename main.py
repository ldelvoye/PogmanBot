import discord
from config import TOKEN



client = discord.Client()


@client.event
async def log_in():
    print("I love Puggi".format(client))


@client.event
async def message():
    if message == "cock":
        print()


client.run(TOKEN)
