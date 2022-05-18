from discord.ext.commands import Cog, Context
from cogs.utils import command


name = 'General'
description = "Those commands that are general-purpose and don't fall into any specific category."
hidden = False

class General(Cog, name=name, description=description, command_attrs=dict(hidden=hidden)):
	"""Cog that contains general-purpose commands for a TTRPGBot.

	Attributes
	----------
	name: Optional[:class:`str`]
		The name of the cog. Defaults to ``General``.
	description: Optional[:class:`str`]
		The description of the cog.
	command_attrs: Optional[:class:`dict`]
		The attributes by default of the commands of the cog. Defaults to ``{'hidden':False}``.
	"""
	
	def __init__(self, bot):
		"""Initializer of the General cog.
		
		Parameters
		----------
		bot: [:class:`Bot`]
			Bot that uses this General cog.
		"""
		
		self.bot = bot

	@command(name='hello', brief="Says hello back", description="Says hello back like a good child would do (in code style)")
	async def hello(self, context:Context):
		"""Says hello to the bot and the bot replies back."""
		
		await context.send("Hello World.")

	@command(name='greet', brief="Greets you back", description="Greets you back like a good child would do (in bot style)")
	async def greet(self, context:Context):
		"""Greets the bot and the bot replies back."""
		
		await context.send("SA-LU-TATIONS!")

	@command(name='replace', brief="Replaces your message", description="Replaces your message because this was me testing how to replace messages")
	async def replace(self, context:Context):
		"""Asks the bot to replace your message with something else and the bot does so."""
		
		await context.message.delete()
		await context.send(f"I am replacing a message by {context.author.name}")

def setup(bot):
	cog = General(bot)
	bot.add_cog(cog)

def teardown(bot):
	bot.remove_cog("General")
