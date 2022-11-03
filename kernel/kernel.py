from aiogram import Dispatcher,  Bot

bot = Bot(token=API_TOKEN)
disp = Dispatcher(bot, storage=MemoryStorage())
