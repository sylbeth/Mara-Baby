from discord import Intents
from discord.ext.commands import Bot, when_mentioned_or
from cogs.pico1046 import Ilyal
from cogs.general import General
from cogs.utils import Utils


command_prefix = when_mentioned_or('ttr')
description = """A multi-purpose bot for all kinds of tabletop role-playing games.
It's a nice child, take care of my child."""
intents = Intents.default()
#intents.message_content = True
strip_after_prefix = True

class TTRPGBot(Bot):
	"""Initializer of the TTRPG bot.
		
	Attributes
	----------
	token: [:class:`string`]
		Token that this TTRPG bot uses.
	command_prefix: [:class:`string`, `list`]
		Prefix(es) for the commands that uses this TTRPG bot.  Defaults to ``when_mentioned_or('ttr')``.
	description: [:class:`str`]
		The description of the bot.
	intents: [:class:`Intents`]
		The intents for the bot to use. Defaults to ``Intents.default()``.
	strip_after_prefix: [:class:`bool`]
		Whether it should skip whitespaces after the prefix or not. Defaults to ``True``.
	"""
	
	def __init__(self, token, command_prefix=command_prefix, description=description, intents=intents, strip_after_prefix = strip_after_prefix):
		"""Initializer of the TTRPG bot.
		
		Parameters
		----------
		token: [:class:`string`]
			Token that this TTRPG bot uses.
		command_prefix: Optional[:class:`string`, `list`]
			Prefix(es) for the commands that uses this TTRPG bot. Defaults to ``when_mentioned_or('ttr')``.
		description: Optional[:class:`str`]
			The description of the bot.
		intents: Optional[:class:`Intents`]
			The intents for the bot to use. Defaults to ``Intents.default()``.
		strip_after_prefix: Optional[:class:`bool`]
			Whether it should skip whitespaces after the prefix or not. Defaults to ``True``.
		"""
		
		super().__init__(command_prefix=command_prefix, description=description, intents=intents, strip_after_prefix=strip_after_prefix)
		self.run(token)
