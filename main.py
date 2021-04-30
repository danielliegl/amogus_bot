# bot.py
import os
from os.path import join, dirname

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

client = discord.Client()

client = commands.Bot(command_prefix='#')
amogus_emoji = discord.utils.get(client.emojis, name='amogus')

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
  if words_re.search(message.content) and (message.author.name != 'Amogus Bot'):
      # await channel.send('amogus')
      await message.add_reaction("<:amogus:832622134009397278>")
      
      
  await client.process_commands(message)

@client.command()
async def say(ctx, arg):
    print('say command ' + arg)
    await ctx.send(arg)

client.run(TOKEN)