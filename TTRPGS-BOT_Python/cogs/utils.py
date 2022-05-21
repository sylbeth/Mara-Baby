from discord.ext.commands import command, group, Cog as SupCog, Context
from discord.ext.commands.errors import ExtensionAlreadyLoaded, ExtensionNotLoaded, ExtensionFailed, NoEntryPointError, ExtensionNotFound
from errors import ExtensionBanned, ExtensionAlreadyBanned, ExtensionNotBanned
from os import listdir
from os.path import join as joinpath, basename


class Cog(SupCog, command_attrs=dict(ignore_extra=False, hidden=False)):
	"""Modification of commands.Cog that changes the default value for ``ignore_extra`` from ``True`` to ``False``."""


class HidCog(SupCog, command_attrs=dict(ignore_extra=False, hidden=True)):
	"""Modification of commands.Cog that changes the default value for ``ignore_extra`` from ``True`` to ``False``."""


def all_extensions_loader(bot):
	cogs_path = joinpath('TTRPGS-BOT_Python','cogs')
	for filename in listdir(cogs_path):
		if filename.endswith('.py'):
			try:
				extension_path = f"cogs.{filename[:-3]}"
				bot.load_extension(extension_path)
				
			except Exception:
				pass

def all_extensions_unloader_full(bot):
	cogs_path = joinpath('TTRPGS-BOT_Python','cogs')
	for filename in listdir(cogs_path):
		if filename.endswith('.py') and filename != 'utils.py':
			try:
				extension_path = f"cogs.{filename[:-3]}"
				bot.unload_extension(extension_path)
				
			except Exception:
				pass


def all_extensions_unloader(bot):
	extensions = list(bot.extensions.keys())
	for extension in extensions:
		if extension != 'cogs.utils':
			try:
				bot.unload_extension(extension)
				
			except Exception:
				pass


def all_extensions_reloader(bot):
	extensions = list(bot.extensions.keys())
	for extension in extensions:
		try:
			bot.reload_extension(extension)
			
		except Exception:
			pass


def all_extensions_banner(bot):
	if hasattr(bot, 'extension_ban_list'):
		ban_list = bot.extension_ban_list[:]
		extensions = list(bot.extensions.keys())
		for extension in extensions:
			if extension != 'cogs.utils':
				try:
					bot.unload_extension(extension)
					
				except Exception:
					pass
				if extension not in ban_list:
					bot.extension_ban_list.append(extension)
	else:
		all_extensions_unloader(bot)


def all_extensions_unbanner(bot):
	if hasattr(bot, 'extension_ban_list'):
		bot.extension_ban_list = list()


class Utils(HidCog, name='Utils', description="Those listeners and commands that are useful to the bot itself."):
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

	@Cog.listener()
	async def on_ready(self):
		"""Triggers whenever the bot is ready and prints its username on console."""
		
		print(f"{self.bot.user.name}'s body is ready")
	
	@group(name='cog', brief="Messes with the cogs system", description="Messes with the cogs system by loading and unloading them", invoke_without_command=True)
	async def cog(self, context:Context):
		"""Edits the cogs that the bot is using."""
		await context.send("Be careful when messing with cogs.")
	
	@cog.command(name='load', brief="Loads an extension for the bot", description="Loads a specified extension for the bot or all of them")
	async def load(self, context:Context, filename):
		"""Loads a new extension for the bot."""
		if filename == 'all':
			all_extensions_loader(self.bot)
			await context.send("All extensions have been loaded.")
		else:
			try:
				self.bot.load_extension(f"cogs.{filename}")
				await context.send(f"The extension {filename} has been successfully loaded.")
			except ExtensionNotFound:
				await context.send(f"The extension {filename} could not be found.")
			except ExtensionAlreadyLoaded:
				await context.send(f"The extension {filename} is already loaded.")
			except NoEntryPointError:
				await context.send(f"The extension {filename} does not have a setup function.")
			except ExtensionFailed:
				await context.send(f"The extension {filename} or its setup function had an execution error.")
			except ExtensionBanned:
				await context.send(f"The extension {filename} has been banned.")

	@cog.command(name='unload', brief="Unloads an extension for the bot", description="Unloads a specified extension for the bot or all of them")
	async def unload(self, context:Context, filename):
		"""Unloads a specific extension for the bot."""
		if filename == 'all':
			all_extensions_unloader(self.bot)
			await context.send("All extensions have been unloaded.")
		elif filename != 'utils':
			try:
				self.bot.unload_extension(f"cogs.{filename}")
				await context.send(f"The extension {filename} has been successfully unloaded.")
			except ExtensionNotLoaded:
				await context.send(f"The extension {filename} is not loaded yet.")
			except ExtensionNotFound:
				await context.send(f"The extension {filename} could not be found.")
		else:
			await context.send("The extension utils cannot be unloaded.")

	@cog.command(name='reload', brief="Reloads an extension for the bot", description="Reloads a specified extension for the bot or all of them")
	async def reload(self, context:Context, filename):
		"""Reloads a specific extension for the bot."""
		if filename == 'all':
			all_extensions_reloader(self.bot)
			await context.send("All extensions have been reloaded.")
		else:
			try:
				self.bot.reload_extension(f"cogs.{filename}")
				await context.send(f"The extension {filename} has been successfully reloaded.")
			except ExtensionNotLoaded:
				await context.send(f"The extension {filename} is not loaded yet.")
			except ExtensionNotFound:
				await context.send(f"The extension {filename} could not be found.")
			except NoEntryPointError:
				await context.send(f"The extension {filename} does not have a setup function.")
			except ExtensionFailed:
				await context.send(f"The extension {filename} or its setup function had an execution error.")

	@cog.command(name='ban', brief="Bans an extension for the bot", description="Bans a specified extension for the bot or all of them")
	async def ban(self, context:Context, filename):
		"""Bans a specific extension for the bot."""
		if filename == 'all':
			all_extensions_banner(self.bot)
			await context.send("All extensions have been banned.")
		elif filename != 'utils':
			try:
				self.bot.ban_extension(f"cogs.{filename}")
				await context.send(f"The extension {filename} has been successfully banned.")
			except ExtensionAlreadyBanned:
				await context.send(f"The extension {filename} has already been banned.")
		else:
			await context.send("The extension utils cannot be banned.")

	@cog.command(name='unban', brief="Unbans an extension for the bot", description="Unbans a specified extension for the bot or all of them")
	async def unban(self, context:Context, filename):
		"""Unbans a specific extension for the bot."""
		if filename == 'all':
			all_extensions_unbanner(self.bot)
			await context.send("All extensions have been unbanned.")
		else:
			try:
				self.bot.unban_extension(f"cogs.{filename}")
				await context.send(f"The extension {filename} has been successfully unbanned.")
			except ExtensionNotBanned:
				await context.send(f"The extension {filename} has not been banned.")

	@cog.command(name='list', brief="Lists all extensions for the bot", description="Lists all extensions for the bot")
	async def list_extensions(self, context:Context):
		"""Lists all the extensions for the bot."""
		extensions = ""
		for extension in self.bot.extensions.keys():
			extensions += extension + '\n'
		await context.send("This are all the loaded extensions:\n" + extensions)

	@cog.command(name='banlist', brief="Lists all banned extensions for the bot", description="Lists all banned extensions for the bot")
	async def banlist(self, context:Context):
		"""Lists all the banned extensions for the bot."""
		if self.bot.extension_ban_list:
			extensions = ""
			for extension in self.bot.extension_ban_list:
				extensions += extension + '\n'
			await context.send("This are all the banned extensions:\n" + extensions)
		else:
			await context.send("There are no banned extensions.")


def setup(bot):
	cog = Utils(bot)
	bot.add_cog(cog)
	bot.help_command.cog = cog

def teardown(bot):
	bot.remove_cog('Utils')
