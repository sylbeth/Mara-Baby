from discord import Intents
from discord.ext.commands import Bot, when_mentioned_or
from errors import ExtensionBanned, ExtensionAlreadyBanned, ExtensionNotBanned
from cogs.utils import all_extensions_loader


command_prefix = when_mentioned_or('ttr')
intents = Intents.default()
#intents.message_content = True

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
	
	def __init__(self, token, command_prefix=command_prefix, description="""A multi-purpose bot for all kinds of tabletop role-playing games.
They are a nice child, take care of my child.""", intents=intents, strip_after_prefix=True):
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
		
		self.extension_ban_list = list()
		all_extensions_loader(self)
		self.run(token)

	def load_extension(self, name, *, package=None):
		"""Loads an extension.

		An extension is a python module that contains commands, cogs, or
		listeners.

		An extension must have a global function, ``setup`` defined as
		the entry point on what to do when the extension is loaded. This entry
		point must have a single argument, the ``bot``.

		Parameters
		------------
		name: :class:`str`
			The extension name to load. It must be dot separated like
			regular Python imports if accessing a sub-module. e.g.
			``foo.test`` if you want to import ``foo/test.py``.
		package: Optional[:class:`str`]
			The package name to resolve relative imports with.
			This is required when loading an extension using a relative path, e.g ``.foo.test``.
			Defaults to ``None``.
		
		Raises
		--------
		ExtensionNotFound
			The extension could not be imported.
			This is also raised if the name of the extension could not
			be resolved using the provided ``package`` parameter.
		ExtensionAlreadyLoaded
			The extension is already loaded.
		NoEntryPointError
			The extension does not have a setup function.
		ExtensionFailed
			The extension or its setup function had an execution error.
		ExtensionBanned
			The exstension has been banned.
		"""
		
		name = self._resolve_name(name, package)
		if name in self.extension_ban_list:
			raise ExtensionBanned(name)
		else:
			super().load_extension(name)
			print(f"Setting up {name}...")

	def unload_extension(self, name, *, package=None):
		"""Unloads an extension.

		When the extension is unloaded, all commands, listeners, and cogs are
		removed from the bot and the module is un-imported.
		
		The extension can provide an optional global function, ``teardown``,
		to do miscellaneous clean-up if necessary. This function takes a single
		parameter, the ``bot``, similar to ``setup`` from
		:meth:`~.Bot.load_extension`.

		Parameters
		------------
		name: :class:`str`
			The extension name to unload. It must be dot separated like
			regular Python imports if accessing a sub-module. e.g.
			``foo.test`` if you want to import ``foo/test.py``.
		package: Optional[:class:`str`]
			The package name to resolve relative imports with.
			This is required when unloading an extension using a relative path, e.g ``.foo.test``.
			Defaults to ``None``.

		Raises
		-------
		ExtensionNotFound
			The name of the extension could not
			be resolved using the provided ``package`` parameter.
		ExtensionNotLoaded
			The extension was not loaded.
		"""

		name = self._resolve_name(name, package)
		super().unload_extension(name)
		print(f"Unloading {name}...")
	
	def ban_extension(self, name, *, package=None):
		"""Bans an extension.

		When the extension is banned, all commands, listeners, and cogs are
		removed from the bot and the module is un-imported if it and added to
		the extension_ban_list.

		The extension can provide an optional global function, ``teardown``,
		to do miscellaneous clean-up if necessary. This function takes a single
		parameter, the ``bot``, similar to ``setup`` from
		:meth:`~.Bot.load_extension`.

		Parameters
		------------
		name: :class:`str`
			The extension name to ban. It must be dot separated like
			regular Python imports if accessing a sub-module. e.g.
			``foo.test`` if you want to import ``foo/test.py``.
		package: Optional[:class:`str`]
			The package name to resolve relative imports with.
			This is required when unloading an extension using a relative path, e.g ``.foo.test``.
			Defaults to ``None``.

		Raises
		-------
		ExtensionAlreadyBanned
			The extension is already banned.
		"""
		
		name = self._resolve_name(name, package)
		if name in self.extension_ban_list:
			raise ExtensionAlreadyBanned(name)
		else:
			self.extension_ban_list.append(name)
			try:
				self.unload_extension(name)
			except Exception:
				pass
	
	def unban_extension(self, name, *, package=None):
		"""Unbans an extension.

		When the extension is unbanned, it can be load again.
		
		Parameters
		------------
		name: :class:`str`
			The extension name to unban. It must be dot separated like
			regular Python imports if accessing a sub-module. e.g.
			``foo.test`` if you want to import ``foo/test.py``.
		package: Optional[:class:`str`]
			The package name to resolve relative imports with.
			This is required when unloading an extension using a relative path, e.g ``.foo.test``.
			Defaults to ``None``.

		Raises
		-------
		ExtensionNotBanned
			The extension was not banned.
		"""
		
		name = self._resolve_name(name, package)
		try:
			self.extension_ban_list.remove(name)
		except ValueError:
			raise ExtensionNotBanned(name)
