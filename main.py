# bot.py
import os
from os.path import join, dirname
import time

import discord
from discord.ext import commands
from discord.utils import get

from config_handler import *
from dictionary import *
import translators as ts

import re
from word_list import amogus_list

# ------------------
# ----INIT STUFF----
# ------------------

amogus_list = improve_wordlist(amogus_list)
words_re = re.compile("|".join(amogus_list))

config = load_cfg()

TOKEN = config['discord_token']
if TOKEN == "":
  print("Enter your Bots Token into settings.json to continue!")
  exit()
GUILD = '15er Steyr'
command_prefix = config['prefix']

client = discord.Client()
client = commands.Bot(command_prefix=command_prefix, help_command=None)
amogus_emoji = discord.utils.get(client.emojis, name='amogus')

# sus(message):
# checks if the given message contains any forbidden words from the previously
# initialized list and returns true. also uses bing translation if it does not
# find any matches.
def sus(message):
  return (words_re.search(message.content.lower()) or words_re.search(ts.bing(message.content).lower())) and message.author.name != "Amogus Bot"

# ----Ready Event----
@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')
  
  print(f'Using prefix {command_prefix}')
  for guild in client.guilds:
      if guild.name == GUILD:
          break

  print(
      f'{client.user} is connected to the following guild:\n'
      f'{guild.name}(id: {guild.id})'
  )

  members = '\n - '.join([member.name for member in guild.members])
  print(f'Guild Members:\n - {members}')
  print('Ende.')

@client.event
async def on_message(message):
  channel = message.channel
  print('i sig nochricht: ' + message.content + " von " + message.author.name)
  if sus(message):
      await message.add_reaction("<:amogus:832622134009397278>")
  await client.process_commands(message)

# ----------------
# ----COMMANDS----
# ----------------

@client.command()
async def say(ctx, arg):
    print('say command ' + arg)
    await ctx.send(arg)

@client.command()
async def help(ctx):
    await ctx.send(f'{client.command_prefix}prefix <arg> - changes the prefix used for this bot\nhttps://www.youtube.com/watch?v=nFstpT_YTro')

# amogus command:
# the bot enters the users voice channel and plays this sound:
# https://www.youtube.com/watch?v=j5B_FqIxo_8
#
@client.command()
async def amogus(ctx):
  if ctx.author.voice and ctx.author.voice.channel:
    channel = ctx.author.voice.channel
  else:
    await ctx.send("You are not connected to a voice channel")
    return
  await channel.connect()

  server = ctx.message.guild
  channel = ctx.author.voice.channel
  voice_client = server.voice_client
  voice_client.play(discord.FFmpegPCMAudio('./media/amogus.mp3'))
  time.sleep(2)
  await voice_client.disconnect()

# prefix command:
# replaces the used prefix for the bot, will change it for all servers atm
# could use a database to store prefixes and other information for multiple
# servers?
@client.command()
async def prefix(ctx, arg):
  config['prefix'] = arg
  update_cfg_file(config)
  client.command_prefix = arg
  await ctx.send(f'Now using this prefix: {arg}')

#----STARTS BOT----
client.run(TOKEN)
