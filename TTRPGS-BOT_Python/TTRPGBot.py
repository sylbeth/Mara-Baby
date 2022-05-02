from discord.ext import commands

class BotExtension(commands.Bot):
	def __init__(self, command_prefix, description):
		super().__init__(command_prefix=command_prefix, description=description)
		self.strip_after_prefix = True
	
	async def on_ready(self):
		print('{0.user.name}\'s body is ready'.format(self))

class TTRPGBot():
	command_prefix = 'ttr'
	description = '''A multi-purpose bot for all kinds of tabletop role-playing games.
	It's a nice child, take care of my child.'''
	bot = BotExtension(command_prefix=command_prefix, description=description)

	@bot.command(name='hello', brief='Says hello back.', description='Says hello back like a good child would do.')
	async def hello(context:commands.Context):
		await context.send('Hello World.')

	@bot.command(name='replace', brief='Replaces your message.', description='Replaces your message because this was me testing how to replace messages.')
	async def replace(context:commands.Context):
		await context.message.delete()
		await context.send('I am replacing a message by {0.author.name}'.format(context))
	
	@bot.command(name='1046', brief='Says hi to their moms.', description='Says hi to either LuLu or Sylbeth.')
	async def replace(context:commands.Context):
		if context.author.id == 245623966088167426 or context.author.id == 680142975078105136:
			await context.send('Hi mom! Hope you are having a nice day, I wuv you!')
		else:
			await context.send('You aren\'t my mom, you shouldn\'t be using this.')