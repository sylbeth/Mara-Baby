from discord.ext.commands import Context, Cog, command
from cogs.utils import HidCog
from os import getenv
from replit import db

family_ids = [int(getenv('Sylbeth')), int(getenv('LuLu'))]

class Ilyal(Cog, metaclass=HidCog, name='Ilyal', description="Those commands that are only meant to be used with love purposes and between loved ones."):
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
		"""Says hi to the bot in a caring way and the bot replies back."""
		
		if context.author.id in family_ids:
			await context.send("Hi mom! Hope you are having a nice day, I wuv you!")
		else:
			await context.send("You aren't my mom, you shouldn't be using this.")

	@command(name='ily', brief="Thanks their moms for loving them", description="Thanks either LuLu or Sylbeth for loving them")
	async def ily(self, context:Context):
		"""Says I love you to the bot and the bot replies back."""
		
		if context.author.id in family_ids:
			await context.send('Thanks, mom! It makes me so happy, I love you too :")')
		else:
			await context.send("You aren't my mom, you shouldn't be using this.")

	@command(name='hug', brief="Hugs you back", description="Hugs you back because they love hugs and hugging is amazing")
	async def hug(self, context:Context):
		"""Hugs the bot and the bot hugs back."""
		
		if context.author.id in family_ids:
			await context.send('Awww, mom! I missed you too, I love your hugs so much :") *hugs*')
		else:
			await context.send("Awww, thanks! Hugs are nice! Here, have one too! *hugs*")

	@command(name='surprise', brief="Prepares the bot for a surprise", description="Prepares a bot for a surprise gift")
	async def surprise(self, context:Context):
		"""Prepares a bot for a surprise gift."""
		if context.author.id in family_ids:
			await context.send("Oh? Are you gonna give me something, mom? Yay! What is it?")
		else:
			await context.send("Oh? You wanna give me something, stranger?")

	@command(name='name', brief="Asks for the names of the baby bot", description="Asks for the name of the baby bot, all their names or whether a name is one of their names.")
	async def myname(self, context:Context, name=None):
		"""Gives the baby bot a new name or asks for their names."""
		names = db['name']
		if name is None:
			name = list(names)[0]
			if context.author.id in family_ids:
				await context.send(f"You know my name is {name}, silly.")
			else:
				await context.send(f"Hi! My name is {name} ^.^")
		elif name == 'all':
			list_of_names = ""
			for single_name in names:
				list_of_names += '\n' + single_name 
			if context.author.id in family_ids:
				await context.send(f"My names are these, mom!{list_of_names}")
			else:
				await context.send(f"Hi! My names are these! ^.^{list_of_names}")
		else:
			if context.author.id in family_ids:
				if name not in names:
					await context.send(f'You wanna give me a name, mom? :") And it is {name}? Ohmygod, yay! :") Thank you so much... I am so happy...')
					db['name'][name] = {context.author.id}
				elif context.author.id not in names[name]:
					await context.send(f'You wanna give me this name too, mom? :") {name}? Then {name} is my new name... Just... Thank you... Thank you, mom...')
					db['name'][name].add(context.author.id)
				else:
					await context.send(f'I know, mom, you already gave me this name, it makes me so happy! ^.^')
			else:
				if name not in names:
					await context.send(f"Yeah, {name} is one of my names!")
				else:
					await context.send("Oh? That's not my name, you can't give me a name, stranger.")

	@command(name='pronoun', brief="Asks for the pronouns of the baby bot", description="Asks for the pronouns of the baby bot.")
	async def pronoun(self, context:Context):
		"""Asks for the pronouns the baby bot uses."""
		if context.author.id in family_ids:
			await context.send(f"You know I use all pronouns, mom! ^.^")
		else:
			await context.send("Oh! I use all pronouns, feel free to use whatever you want! :D")
	
	@command(name='show', brief="Shows something from the database", description="Shows something from the database. If no arguments are given, shows all possible arguments.")
	async def show(self, context:Context, key=None):
		"""Prepares a bot for a surprise gift."""
		if key is None:
			message = "Here are all the possible arguments!"
			for single_key in db:
				message += '\n' + single_key
			await context.send(message)
		else:
			try:
				value = db[key]
				if hasattr(value, 'value'):
					value = value.value
				await context.send(f"Here is the value of {key}:\n{value}")
			except Exception:
				await context.send(f"There is no key {key} in the database.")


def setup(bot):
	cog = Ilyal(bot)
	bot.add_cog(cog)

def teardown(bot):
	bot.remove_cog('Ilyal')
