from aiogram.contrib.fsm_storage.memory import MemoryStorage

import Token
from aiogram import Bot, Dispatcher

bot = Bot(token=Token.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
