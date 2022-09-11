import discord
import os
# Following imports are from our own files
import dice as dicePY
import databse as databasePY

# Create a discord bot client with default permission given
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Create the dice
dice = dicePY.Dice()

# Create the databse
database = databasePY.MemberDataBase()


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

    if message.content.startswith(".st "):
      amount = database.addPlayer(message)
      await message.channel.send("收到{}条属性".format(amount))

    if message.content.startswith(".chk"):
      type, result = database.checkStatus(message)
      await message.channel.send("查询 {} 为 {}".format(type, result))


client.run(os.getenv('TOKEN'))