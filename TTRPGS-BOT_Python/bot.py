import discord
from discord.ext import commands
import os

command_prefix = 'ttr'
description = '''A multi-purpose bot for all kinds of tabletop role-playing games.
It's a nice child, take care of my child.'''

bot = commands.Bot(command_prefix=commands.when_mentioned_or(command_prefix), description=description)

bot.strip_after_prefix = True

@bot.event
async def on_ready():
	print('{0.user.name}\'s body is ready'.format(bot))

@bot.command(name='hello', brief='Says hello back.', description='Says hello back like a good child would do.')
async def hello(context:commands.Context):
	await context.send('Hello World.')

@bot.command(name='replace', brief='Replaces your message.', description='Replaces your message because this was me testing how to replace messages.')
async def replace(context:commands.Context):
	await context.message.delete()
	await context.send('I am replacing a message by {0.author}'.format(context))

bot.run(os.getenv('TOKEN'))