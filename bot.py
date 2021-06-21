from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from environs import Env
from tgbot.__main__ import startup

# Read env file

env = Env()
env.read_env()

token = env.str("BOT_TOKEN")

# Bot, storage and dispatcher instances
bot = Bot(token=token, parse_mode='html')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

if __name__ == "__main__":
    # Start long-polling mode
    executor.start_polling(dp, on_startup=startup, skip_updates=True)
