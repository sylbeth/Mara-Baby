from discord import Intents
from discord.ext.commands import Bot
from Cogs.pico1046 import PICO1046
from Cogs.general import General

command_prefix = 'ttr'
description = '''A multi-purpose bot for all kinds of tabletop role-playing games.
It's a nice child, take care of my child.'''
intents = Intents.default()

class TTRPGBot(Bot):
	def __init__(self, token, command_prefix=command_prefix, description=description, intents=intents):
		super().__init__(command_prefix=command_prefix, description=description, intents=intents)
		self.strip_after_prefix = True
		self.add_cog
		self.add_cog(PICO1046(self))
		general = General(self)
		self.add_cog(general)
		self.help_command.cog = general
		self.run(token)
	
	async def on_ready(self):
		print('{0.user.name}\'s body is ready'.format(self))