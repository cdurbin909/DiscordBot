import discord
import lenny
from discord.ext import commands
from pyrandmeme import *
import os

client = discord.Client()

# I added this comment for a test


def sponge_word(word):
    yep = ''
    i = True
    for char in word:
        if i:
            yep += char.upper()
        else:
            yep += char.lower()
        if char != ' ':
            i = not i
    return yep


@client.event
async def on_ready():
    print('bot is ready')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$sponge'):
        sponge = msg.split('$sponge ', 1)[1]
        await message.channel.send(sponge_word(sponge))

    if msg.startswith('$lenny'):
        await message.channel.send(lenny.lenny())

    if msg.startswith('$meme'):
        await message.channel.send(embed=await pyrandmeme())


client.run(os.environ.get('discord bot key'))
