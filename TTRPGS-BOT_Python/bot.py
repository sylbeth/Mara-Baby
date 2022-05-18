from TTRPGBot import TTRPGBot
from os import getenv, getcwd
from os.path import join as joinpath
from logging import getLogger, DEBUG, FileHandler, Formatter


def set_log():
	"""Setter of the log at the ``discord.log`` file."""
	
	logger = getLogger('discord')
	logger.setLevel(DEBUG)
	
	handler = FileHandler(filename=joinpath('TTRPGS-BOT_Python','temp','discord.log'), encoding='utf-8', mode='w')
	handler.setFormatter(Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
	logger.addHandler(handler)


def start_bot():
	"""Sets the log for the TTRPGBot and starts running it."""
	set_log()
	bot = TTRPGBot(getenv('TOKEN'))

start_bot()