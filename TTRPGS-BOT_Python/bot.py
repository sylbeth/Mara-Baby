from TTRPGBot import TTRPGBot
from os import getenv
from logging import getLogger, DEBUG, FileHandler, Formatter

logger = getLogger('discord')
logger.setLevel(DEBUG)
handler = FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = TTRPGBot(getenv('TOKEN'))