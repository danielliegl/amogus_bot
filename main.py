# bot.py
import os
from os.path import join, dirname
import time
import youtube_dl

import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

import re
from word_list import amogus_list
words_re = re.compile("|".join(amogus_list))

dotenv_path = join(dirname(__file__), '.env')
load_dotenv()
TOKEN = os.environ.get("DISCORD_TOKEN")
GUILD = '15er Steyr'

sound_ready = True

client = discord.Client()
client = commands.Bot(command_prefix='#')
amogus_emoji = discord.utils.get(client.emojis, name='amogus')

# check if message contains any forbidden words
def sus(message):
  return words_re.search(message.content.lower()) and message.author.name != "Amogus Bot"

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')
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

@client.command()
async def say(ctx, arg):
    print('say command ' + arg)
    await ctx.send(arg)

@client.command()
async def amogus(ctx):
  if sound_ready:
    sound_ready = False
    if ctx.author.voice and ctx.author.voice.channel:
      channel = ctx.author.voice.channel
    else:
      await ctx.send("You are not connected to a voice channel")
      return
    await channel.connect()

    server = ctx.message.guild
    channel = ctx.author.voice.channel
    voice_client = server.voice_client
    voice_client.play(discord.FFmpegPCMAudio('amogus.mp3'))
    time.sleep(2)
    await voice_client.disconnect()
    sound_ready = True
  else:
    ctx.send("Not ready yet.")

client.run(TOKEN)