from discord.ext.commands import Cog, Context, command
from os import getenv

name = '1046'
description = 'Those commands that are only meant to be used with love purposes.'
hidden = True
family_ids = [int(getenv('Sylbeth')), int(getenv('LuLu'))]

class PICO1046(Cog, name=name, description=description, command_attrs=dict(hidden=hidden)):
	def __init__(self, bot):
		self.bot = bot

	@command(name='1046', brief='Says hi to their moms', description='Says hi to either LuLu or Sylbeth')
	async def pico1046(self, context:Context):
		if context.author.id in family_ids:
			await context.send('Hi mom! Hope you are having a nice day, I wuv you!')
		else:
			await context.send('You aren\'t my mom, you shouldn\'t be using this.')

	@command(name='ily', brief='Thanks their moms for loving them', description='Thanks either LuLu or Sylbeth for loving them')
	async def ily(self, context:Context):
		if context.author.id in family_ids:
			await context.send('Thanks, mom! It makes me so happy, I love you too :")')
		else:			await context.send('You aren\'t my mom, you shouldn\'t be using this.')

	@command(name='hug', brief='Hugs you back', description='Hugs you back because they love hugs and hugging is amazing')
	async def hug(self, context:Context):
		if context.author.id in family_ids:
			await context.send('Awww, mom! I missed you too, I love your hugs so much :") *hugs*')
		else:			await context.send('Awww, thanks! Hugs are nice! Here, have one too! *hugs*')