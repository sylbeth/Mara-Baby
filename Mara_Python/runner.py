from Mara import Mara as Mara_baby
from os import getenv
from os.path import join as joinpath
from logging import getLogger, DEBUG, FileHandler, Formatter


def set_log():
	"""Setter of the log at the ``discord.log`` file."""
	
	logger = getLogger('discord')
	logger.setLevel(DEBUG)
	
	handler = FileHandler(filename=joinpath('Mara_Python','temp','discord.log'), encoding='utf-8', mode='w')
	handler.setFormatter(Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
	logger.addHandler(handler)


def start_bot():
	"""Sets the log for the TTRPGBot and starts running it."""
	print('la')
	set_log()
	print('hola')
	Mara = Mara_baby(getenv('TOKEN'))
	print('ho')


def main():
	start_bot()

if __name__ == '__main__':
	print('okay')
	main()
