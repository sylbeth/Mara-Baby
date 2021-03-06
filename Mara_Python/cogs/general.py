from discord.ext.commands import Context, command, Bot
from cogs.utils import PubCog


class General(PubCog, name='General', description="Those commands that are general-purpose and don't fall into any specific category."):
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

    def __init__(self, bot: Bot) -> None:
        """Initializer of the General cog.
        
        Parameters
        ----------
        bot: [:class:`Bot`]
            Bot that uses this General cog.
        """

        self.bot: Bot = bot

    @command(name='hello', brief="Says hello back", description="Says hello back like a good child would do (in code style)")
    async def hello(self, context: Context) -> None:
        """Says hello to the bot and the bot replies back."""

        await context.send("Hello World.")

    @command(name='greet', brief="Greets you back", description="Greets you back like a good child would do (in bot style)")
    async def greet(self, context: Context) -> None:
        """Greets the bot and the bot replies back."""

        await context.send("SA-LU-TATIONS!")

    @command(name='replace', brief="Replaces your message", description="Replaces your message because this was me testing how to replace messages")
    async def replace(self, context: Context) -> None:
        """Asks the bot to replace your message with something else and the bot does so."""

        await context.message.delete()
        await context.send(f"I am replacing a message by {context.author.name}")


def setup(bot) -> None:
    cog: General = General(bot)
    bot.add_cog(cog)

def teardown(bot) -> None:
    bot.remove_cog('General')
