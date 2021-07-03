import textwrap

import discord
import random
import lenny
from discord.ext import commands
from pyrandmeme import *
import os
import json
import requests

client = discord.Client()

dad_mode = False
responses = True

commands = '`$sponge + message: returns message in sponge case\n' \
           '$lenny: returns a random lenny face\n' \
           '$meme: returns a random meme\n' \
           '$dadmode + (on/off): changes the state of dadmode\n' \
           '(try saying "im hungry")\n' \
           '$responses + (on/off): changes if the bot will respond\n`'

eightball = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it',
             'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again',
             'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
             'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']


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

    if msg.startswith('$8ball') and responses:
        question = msg.split('$8ball ', 1)[1]
        if question == '' or question == ' ':
            await message.channel.send('please type a question')
        else:
            await message.channel.send(random.choice(eightball))

    if msg.startswith('$epic'):
        rate = random.randint(1, 101)
        if rate < 20:
            end = 'You are very UNepic!'
        if 40 > rate > 20:
            end = 'That\'s not very epic!'
        if 60 > rate > 40:
            end = 'You\'re about half epic!'
        if 80 > rate > 60:
            end = 'Heyyy you\'re pretty epic!'
        if 99 > rate > 80:
            end = 'You\'re more than just epic, you\'re elite!'
        if rate == 100:
            end = 'I BOW BEFORE YOU ALMIGHTY EPIC ONE!'
        await message.channel.send('You are ' + str(rate) + '% epic! ' + end)

    if msg.startswith('$showerthoughts'):
        randompost = random.randint(1, 20)
        url = requests.get('https://www.reddit.com/r/showerthoughts/hot.json',
                           headers={'User-agent': 'Showerthoughtbot 0.1'})

        thot = json.loads(url.text)

        await message.channel.send(textwrap.fill((thot['data']['children'][randompost]['data']['title'])))

    if msg.startswith('$help'):
        await message.channel.send(commands)


client.run(os.environ.get('BOT_KEY'))
