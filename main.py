# This example requires the 'message_content' intent.

import discord
import json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if  '狗勾' in message.content:
        await message.channel.send('汪！')

with open("token.json", "r") as tokenFile:
    token = json.load(tokenFile)["TOKEN"]

client.run(token)
