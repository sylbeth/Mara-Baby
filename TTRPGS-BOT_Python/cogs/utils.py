from discord.ext.commands import command as supcommand, group as supgroup, Cog, Context


def command(ignore_extra=False, **attrs):
	"""Modification of commands.command that changes the default value for ``ignore_extra`` from ``True`` to 		``False``.

	Parameters
	----------
	ignore_extra: Optional[:class:`bool`]
		Whether or not the command should ignore extra attributes. Defaults to ``{'hidden':True}``.

	Returns
	-------
	Callable[..., :class:`Command`]
		A decorator that converts the provided method into a Command, adds it to the bot, then returns it.
	
	See Also
    --------
    :func:`commands.command`
	"""
	
	def decorator(func):
		return supcommand(ignore_extra=ignore_extra, **attrs)(func)
	
	return decorator


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

	@Cog.listener()
	async def on_ready(self):
		"""Triggers whenever the bot is ready and prints its username on console."""
		
		print(f"{self.bot.user.name}'s body is ready")

def setup(bot):
	cog = Utils(bot)
	bot.add_cog(cog)
	bot.help_command.cog = cog

def teardown(bot):
	bot.remove_cog("Utils")
	bot.help_command.cog = None
