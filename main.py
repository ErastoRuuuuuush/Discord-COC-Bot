import discord
import os
# Following imports are from our own files
import dice as dicePY

# Create a discord bot client with default permission given
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Create the dice
dice = dicePY.Dice()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("小勾"):
        await message.channel.send("汪!")
    if message.content.startswith(".r"):
        response = "汪!【{}】 掷骰 1D{}={}".format(message.author.nick, dice.max, dice.rowDice())
        await message.channel.send(response)

client.run(os.getenv('TOKEN'))