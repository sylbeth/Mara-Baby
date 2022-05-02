from TTRPGBot import TTRPGBot
import os

bot = TTRPGBot().bot

bot.run(os.getenv('TOKEN'))