from aiogram import executor
from aiogram.dispatcher.filters import Command

from config import dp
from handlers.payment_system import buy, pre_checkout_query, successful_payment
from aiogram.types.message import ContentType
from handlers.file import get_file, read_file, FileState


def register_bot_message_handler():
    dp.register_message_handler(buy, Command('buy'))
    dp.register_pre_checkout_query_handler(pre_checkout_query, lambda query: True)
    dp.register_message_handler(successful_payment, content_types=ContentType.SUCCESSFUL_PAYMENT)
    dp.register_message_handler(get_file, Command("savefile"))
    dp.register_message_handler(read_file, state="FileState.waiting_for_file")
    # dp.register_message_handler(echo)


if __name__ == '__main__':
    register_bot_message_handler()
    print('Start')
    executor.start_polling(dp, skip_updates=False)
