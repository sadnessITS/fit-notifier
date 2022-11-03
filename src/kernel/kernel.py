import logging
from aiogram import Dispatcher, Bot
from kernel.config import API_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot, storage=MemoryStorage())
