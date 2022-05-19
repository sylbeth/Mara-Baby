from discord.ext.commands import command, group, Cog as SupCog, Context
from discord.ext.commands.errors import ExtensionAlreadyLoaded, ExtensionNotLoaded, ExtensionFailed, NoEntryPointError, ExtensionNotFound
from os import listdir
from os.path import join as joinpath, basename


class Cog(SupCog, command_attrs=dict(ignore_extra=False)):
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

def all_extensions_unloader(bot):
	cogs_path = joinpath('TTRPGS-BOT_Python','cogs')
	for filename in listdir(cogs_path):
		if filename.endswith('.py') and filename != 'utils.py':
			try:
				extension_path = f"cogs.{filename[:-3]}"
				bot.unload_extension(extension_path)
				
			except Exception:
				pass


name = 'Utils'
description = "Those listeners and commands that are useful to the bot itself."
hidden = True

class Utils(SupCog, name=name, description=description, command_attrs=dict(hidden=hidden,ignore_extra=False)):
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
		
		all_extensions_loader(self.bot)
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
			except ExtensionNotFound:
				await context.send(f"The extension {filename} could not be found.")
			except ExtensionNotLoaded:
				await context.send(f"The extension {filename} is not loaded yet.")
		else:
			await context.send("The extension utils cannot be unloaded.")


def setup(bot):
	print(f"Setting up {basename(__file__)}...")
	cog = Utils(bot)
	bot.add_cog(cog)
	bot.help_command.cog = cog

def teardown(bot):
	print(f"Unloading {basename(__file__)}...")
	bot.remove_cog('Utils')
	bot.help_command.cog = None
	all_extensions_unloader(bot)
