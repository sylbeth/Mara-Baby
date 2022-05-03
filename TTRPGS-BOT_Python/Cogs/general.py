from discord.ext.commands import Cog, Context, command

name = 'General'
description = 'Those commands that don\'t fall into any specific category.'
hidden = False

class General(Cog, name=name, description=description, command_attrs=dict(hidden=hidden)):
	def __init__(self, bot):
		self.bot = bot

	@command(name='hello', brief='Says hello back', description='Says hello back like a good child would do (in code style)')
	async def hello(self, context:Context):
		await context.send('Hello World.')

	@command(name='greet', brief='Greets you back', description='Greets you back like a good child would do (in bot style)')
	async def greet(self, context:Context):
		await context.send('SA-LU-TATIONS!')

	@command(name='replace', brief='Replaces your message', description='Replaces your message because this was me testing how to replace messages')
	async def replace(self, context:Context):
		await context.message.delete()
		await context.send('I am replacing a message by {0.author.name}'.format(context))