import textwrap
import random
from discord.ext import commands
import lenny as a
from pyrandmeme import *
import os
import json
import requests

# client = discord.Client()

responses = True
# filter = False

commands1 = '`$sponge + message: returns message in sponge case\n' \
            '$lenny: returns a random lenny face\n' \
            '$meme: returns a random meme\n' \
            '$dadmode + (on/off): changes the state of dadmode\n' \
            '(try saying "im hungry")\n' \
            '$responses + (on/off): changes if the bot will respond\n' \
            '$8ball + "your question": responds to your question\n' \
            '$epic: returns your epic rate\n' \
            '$showerthoughts: returns a random showerthought\n' \
            '$filter: toggles the filter (off by default)\n' \
            '$add_filter + word: adds the word to the filter list\n' \
            '$dm + user + message: sends the specified user a dm\n' \
            '$clear + amount: clears a certain amount of messages`'

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


client = commands.Bot(command_prefix='$')

client.dad = False
client.responses = True


client.remove_command('help')


# client.filter = False


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('help'))
    print('Bot is ready')


@client.command()
async def help(ctx):
    await ctx.channel.send(commands1)


@client.command()
async def sponge(ctx, *, word):
    if client.responses:
        await ctx.channel.send('`' + sponge_word(word) + '`')


@client.command()
async def lenny(ctx):
    if client.responses:
        await ctx.channel.send('`' + a.lenny() + '`')


@client.command()
async def meme(ctx):
    if client.responses:
        await ctx.channel.send(embed=await pyrandmeme())


@client.command()
async def dadmode(ctx):
    if client.responses:
        if not client.dad:
            dad = True
            await ctx.channel.send('dadmode has been enabled')
        elif client.dad:
            dad = False
            await ctx.channel.send('dadmode has been disabled')


@client.event
async def on_message(message):
    # global filter
    # global responses
    if message.author == client.user:
        return

    msg = message.content

    # if msg.startswith('im') and dad_mode and responses:
    if (' im ' in message.content or msg.startswith('im')) and client.responses:
        dad = msg.split('im ', 1)[1]
        await message.channel.send('`Hi ' + dad + ', I\'m dad!`')

    # if msg.startswith('Im') and dad_mode and responses:
    if (' Im ' in message.content or msg.startswith('Im')) and client.responses:
        dad = msg.split('Im ', 1)[1]
        await message.channel.send('`Hi ' + dad + ', I\'m dad!`')

    # if msg.startswith("i'm") and dad_mode and responses:
    if (' i\'m ' in message.content or msg.startswith("i'm")) and client.responses:
        dad = msg.split("i'm ", 1)[1]
        await message.channel.send('`Hi ' + dad + ', I\'m dad!`')

    # if msg.startswith("i’m") and dad_mode and responses:
    if (' i’m ' in message.content or msg.startswith("i’m")) and client.responses:
        dad = msg.split("i’m ", 1)[1]
        await message.channel.send('`Hi ' + dad + ', I\'m dad!`')

    # if msg.startswith("I'm") and dad_mode and responses:
    if (' I\'m ' in message.content or msg.startswith("I'm")) and client.responses:
        dad = msg.split("I'm ", 1)[1]
        await message.channel.send('`Hi ' + dad + ', I\'m dad!`')

    # if msg.startswith("I’m") and dad_mode and responses:
    if (' I’m ' in message.content or msg.startswith("I’m")) and client.responses:
        dad = msg.split("I’m ", 1)[1]
        await message.channel.send('`Hi ' + dad + ', I\'m dad!`')

    # if client.filter:
    #     text_file = open("\\DiscordBot\\curses", "r")
    #     lines = text_file.read().split(',')
    #     for word in lines:
    #         if word in message.content:
    #             await message.delete()
    #             await message.channel.send(f'{message.author.mention}`Woah there, the filter is on!`')
    #     text_file.close()

    await client.process_commands(message)


@client.command()
async def responses(ctx):
    if client.responses:
        client.responses = False
        await ctx.channel.send('Responses have been disabled')
    else:
        client.responses = True
        await ctx.channel.send('Responses have been enabled')


@client.command(name='8ball')
async def _8ball(ctx):
    await ctx.channel.send('`' + random.choice(eightball) + '`')


@client.command()
async def epic(ctx):
    end = ''
    rate = random.randint(1, 101)
    if rate < 20:
        end = 'You are very UNepic!`'
    if 40 > rate > 20:
        end = 'That\'s not very epic!`'
    if 60 > rate > 40:
        end = 'You\'re about half epic!`'
    if 80 > rate > 60:
        end = 'Heyyy you\'re pretty epic!`'
    if 99 > rate > 80:
        end = 'You\'re more than just epic, you\'re elite!`'
    if rate == 100:
        end = 'I BOW BEFORE YOU ALMIGHTY EPIC ONE!`'
    await ctx.channel.send('`You are ' + str(rate) + '% epic! ' + end)


@client.command()
async def showerthoughts(ctx):
    randompost = random.randint(1, 20)
    url = requests.get('https://www.reddit.com/r/showerthoughts/hot.json',
                       headers={'User-agent': 'Showerthoughtbot 0.1'})

    thot = json.loads(url.text)

    await ctx.channel.send(textwrap.fill(('`' + thot['data']['children'][randompost]['data']['title'] + '`')))


# @client.command()
# async def filter(ctx):
#     if client.filter:
#         client.filter = False
#         await ctx.channel.send('`The filter is now off!`')
#     else:
#         client.filter = True
#         await ctx.channel.send('`The filter is now on!`')


# @client.command()
# @commands.has_permissions(manage_messages=True)
# async def add_filter(ctx, word):
#     await ctx.channel.purge(limit=1)
#     text_file = open("\\DiscordBot\\curses", "a")
#     text_file.write(',' + word)
#     text_file.close()
#     await ctx.channel.send('Word added to filter list!')


@client.command(help='sends the specified user a dm')
async def dm(ctx, member: discord.Member, *, message):
    channel = await member.create_dm()
    await channel.send(message)
    await ctx.channel.send('message sent!')


@client.command(aliases=['c'], help='clears a specified amount of messages\ndefault is 1')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount + 1)


@client.command(help='kicks a specified member.\nreason is listed in kick dm')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="no reason provided"):
    await member.send(f'You have been kicked from {ctx.message.guild.name}, because ' + reason)
    await member.kick(reason=reason)


client.run(os.environ.get('BOT_KEY'))
