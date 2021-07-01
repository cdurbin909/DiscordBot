import discord
import lenny
from discord.ext import commands
from pyrandmeme import *
import os


client = discord.Client()

dad_mode = False
responses = True

commands = '`$sponge + message: returns message in sponge case\n' \
           '$lenny: returns a random lenny face\n' \
           '$meme: returns a random meme\n' \
           '$dadmode + (on/off): changes the state of dadmode\n' \
           '(try saying "im hungry")\n' \
           '$responses + (on/off): changes if the bot will respond\n`'


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
    global dad_mode
    global responses
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$sponge') and responses:
        sponge = msg.split('$sponge ', 1)[1]
        await message.channel.send(sponge_word(sponge))

    if msg.startswith('$lenny') and responses:
        await message.channel.send(lenny.lenny())

    if msg.startswith('$meme') and responses:
        await message.channel.send(embed=await pyrandmeme())

    if msg.startswith('$dadmode on') and responses:
        dad_mode = True
        await message.channel.send('dad mode enabled')

    if msg.startswith('$dadmode off') and responses:
        dad_mode = False
        await message.channel.send('dad mode disabled')

    if msg.startswith('im') and dad_mode and responses:
        dad = msg.split('im ', 1)[1]
        await message.channel.send('Hi ' + dad + ', I\'m dad!')

    if msg.startswith('Im') and dad_mode and responses:
        dad = msg.split('Im ', 1)[1]
        await message.channel.send('Hi ' + dad + ', I\'m dad!')

    if msg.startswith("i'm") and dad_mode and responses:
        dad = msg.split("i'm ", 1)[1]
        await message.channel.send('Hi ' + dad + ', I\'m dad!')

    if msg.startswith("i’m") and dad_mode and responses:
        dad = msg.split("i’m ", 1)[1]
        await message.channel.send('Hi ' + dad + ', I\'m dad!')

    if msg.startswith("I'm") and dad_mode and responses:
        dad = msg.split("I'm ", 1)[1]
        await message.channel.send('Hi ' + dad + ', I\'m dad!')

    if msg.startswith("I’m") and dad_mode and responses:
        dad = msg.split("I’m ", 1)[1]
        await message.channel.send('Hi ' + dad + ', I\'m dad!')

    if msg.startswith('$responses off'):
        responses = False

    if msg.startswith('$responses on'):
        responses = True

    if msg.startswith('$help'):
        await message.channel.send(commands)


client.run(os.environ.get('discord bot key'))


