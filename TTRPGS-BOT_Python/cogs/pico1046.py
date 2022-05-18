from discord.ext.commands import Cog, Context
from cogs.utils import command
from os import getenv


name = 'Ilyal'
description = "Those commands that are only meant to be used with love purposes and between loved ones."
hidden = True
family_ids = [int(getenv('Sylbeth')), int(getenv('LuLu'))]

class Ilyal(Cog, name=name, description=description, command_attrs=dict(hidden=hidden)):
	"""Cog that contains secret, special commands for a TTRPGBot.

	Attributes
	----------
	name: Optional[:class:`str`]
		The name of the cog. Defaults to ``Ilyal``.
	description: Optional[:class:`str`]
		The description of the cog.
	command_attrs: Optional[:class:`dict`]
		The attributes by default of the commands of the cog. Defaults to ``{'hidden':True}``.
	"""
	
	def __init__(self, bot):
		"""Initializer of the Ilyal cog.
		
		Parameters
		----------
		bot: [:class:`Bot`]
			Bot that uses this Ilyal cog.
		"""
		
		self.bot = bot

	@command(name='1046', brief="Says hi to their moms", description="Says hi to either LuLu or Sylbeth")
	async def pico1046(self, context:Context):
		"""Says hi to the bot in a caring way and the bot replies back.
		
		Parameters
		----------
		context: [:class:`Context`]
			Context in which the command has been called.
		"""
		
		if context.author.id in family_ids:
			await context.send("Hi mom! Hope you are having a nice day, I wuv you!")
		else:
			await context.send("You aren't my mom, you shouldn't be using this.")

	@command(name='ily', brief="Thanks their moms for loving them", description="Thanks either LuLu or Sylbeth for loving them")
	async def ily(self, context:Context):
		"""Says I love you to the bot and the bot replies back.
		
		Parameters
		----------
		context: [:class:`Context`]
			Context in which the command has been called.
		"""
		
		if context.author.id in family_ids:
			await context.send('Thanks, mom! It makes me so happy, I love you too :")')
		else:
			await context.send("You aren't my mom, you shouldn't be using this.")

	@command(name='hug', brief="Hugs you back", description="Hugs you back because they love hugs and hugging is amazing")
	async def hug(self, context:Context):
		"""Hugs the bot and the bot hugs back.
		
		Parameters
		----------
		context: [:class:`Context`]
			Context in which the command has been called.
		"""
		
		if context.author.id in family_ids:
			await context.send('Awww, mom! I missed you too, I love your hugs so much :") *hugs*')
		else:
			await context.send("Awww, thanks! Hugs are nice! Here, have one too! *hugs*")