from kernel.kernel import dispatcher
from aiogram import executor

if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)
