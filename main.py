import discord


TOKEN = "ODg4MTg2MzQ3NTkwOTM4NjY2.YUPB_g.0dsPjWvfow3vqguvlirGG-wdvMM"

client = discord.Client()


@client.event
async def log_in():
    print("I love Puggi".format(client))


@client.event
async def message():
    if message == "cock":
        print()


client.run(TOKEN)
