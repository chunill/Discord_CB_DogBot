# This example requires the 'message_content' intent.

import discord
import json
from random import choice

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

dog_name = '狗勾'


def choice_word(words: list[str]):
    return choice(words)


def happy_word():
    words = ['開心', '快樂', '高興', '愉快', '雀躍']
    return choice_word(words)


def happy_action():
    words = ['搖尾巴', '甩動尾巴', '瘋狂搖尾巴']
    return choice_word(words)


def run_action():
    words = ['跑', '衝', '飛奔', '奔']
    return choice_word(words)


def woof_word():
    words = ['汪', '汪汪']
    return choice_word(words)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if dog_name in message.content or '過來' in message.content:
        sentences = [f'{run_action()}過來', f'{happy_word()}地{run_action()}過來']
        await message.channel.send(f'（{choice(sentences)}）')

    if '摸' in message.content:
        sentences = ['🥰', f'（{happy_action()}）', f'🥰（{happy_action()}）', '（用頭蹭手）', '（把臉塞進你掌心）', '（一臉滿足）']
        await message.channel.send(choice(sentences))

    if '握手' in message.content:
        sentences1 = ['', f'{woof_word()}！']
        sentences2 = ['', f'並{happy_action()}', f'一邊{happy_action()}']
        await message.channel.send(choice(sentences1) + '（把爪子放你手上' + choice(sentences2) + '）')

    if '抱' in message.content:
        sentences1 = ['', f'{woof_word()}！（', f'（{happy_word()}', f'{woof_word()}！（{happy_word()}']
        sentences2 = ['撲進你懷裡', '把臉塞到你懷中', '整隻撲到你身上']
        sentences3 = ['', f'，{happy_action()}', f'一邊{happy_action()}']
        await message.channel.send(choice(sentences1) + choice(sentences2) + choice(sentences3) + '）')

    if dog_name in message.content:
        await message.channel.send(f'{woof_word()}！')


with open("token.json", "r") as tokenFile:
    token = json.load(tokenFile)["TOKEN"]

client.run(token)
