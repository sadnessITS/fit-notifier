from core.core import dispatcher
from aiogram import executor
from handlers import init_handlers

if __name__ == "__main__":
    init_handlers()
    executor.start_polling(dispatcher, skip_updates=True)
