import discord
from discord.ext import commands

command_prefix = 'ttr'
description = '''A multi-purpose bot for all kinds of tabletop role-playing games.
It's a nice child, take care of my child.'''
intents = discord.Intents.default()
intents.members = True

class TTRPGBot(commands.Bot):
     def __init__(self, command_prefix = command_prefix, description = description, intents = intents):
         super().__init__(command_prefix, description, intents)