import discord
from discord.ext import commands


class TTRPGBot(commands.Bot):
	def __init__(self, command_prefix=commands.when_mentioned_or('ttr'), description=
	'''A multi-purpose bot for all kinds of tabletop role-playing games.
	It's a nice child, take care of my child.'''):
		super().__init__(command_prefix=command_prefix, description=description)
		self.strip_after_prefix = True
	
	async def on_ready(self):
		print('{0.user.name}\'s body is ready'.format(self))
	
	@commands.command(name='hello', brief='Says hello back.', description='Says hello back like a good child would do.')
	async def hello(context:commands.Context):
		await context.send('Hello World.')

	@commands.command(name='replace', brief='Replaces your message.', description='Replaces your message because this was me testing how to replace messages.')
	async def replace(context:commands.Context):
		await context.message.delete()
		await context.send('I am replacing a message by {0.author}'.format(context))