from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

with open("../Bot/token.txt", "r") as file:
    TOKEN = str(file.read())
    BOT = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)

dispatcher = Dispatcher(BOT, storage=storage)