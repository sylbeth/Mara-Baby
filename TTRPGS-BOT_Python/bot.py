import discord
from discord.ext import commands
import os

command_prefix = 'ttr '
description = '''A multi-purpose bot for all kinds of tabletop role-playing games.
It's a nice child, take care of my child.'''
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=command_prefix, description=description, intents=intents)

@bot.event
async def on_ready():
	print('{0.user.name}\'s body is ready'.format(bot))

@bot.command()
async def hello(context):
	await context.send('Hello World')

@bot.command()
async def replace(context):
	await context.message.delete()
	await context.send('I am replacing your message')

bot.run(os.getenv('TOKEN'))