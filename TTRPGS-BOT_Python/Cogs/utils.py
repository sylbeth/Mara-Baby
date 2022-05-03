from discord.ext.commands import command as supcommand, group as supgroup, Cog





name = 'Utils'
description = "Those listeners and commands that are useful to the bot itself."
hidden = True

class Utils(Cog, name=name, description=description, command_attrs=dict(hidden=hidden)):
	"""Cog that contains utilities and useful listeners for a TTRPGBot.

	Attributes
	----------
	name: Optional[:class:`str`]
		The name of the cog. Defaults to ``Utils``.
	description: Optional[:class:`str`]
		The description of the cog.
	command_attrs: Optional[:class:`dict`]
		The attributes by default of the commands of the cog. Defaults to ``{'hidden':True}``.
	"""
	
	def __init__(self, bot):
		"""Initializer of the Utils cog.
		
		Parameters
		----------
		bot: [:class:`Bot`]
			Bot that uses this Utils cog.
		"""
		
		self.bot = bot

	
	async def on_ready(self):
		"""Triggers whenever the bot is ready and prints its username on console."""
		
		print(f"{self.user.name}'s body is ready")