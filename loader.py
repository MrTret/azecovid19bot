from os import getenv
from sys import exit

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config

TOKEN = config.BOT_TOKEN
if not TOKEN:
    exit("Error: no BOT_TOKEN provided.")


bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

