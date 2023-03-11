import Token
from handlers.base_functions import *
from aiogram import Bot, Dispatcher, executor, types

from config import bot, dp

from handlers.payment_system import *

from aiogram.types.message import ContentType   # to delete

from handlers.file import *


# #get file 2
# import os
# from aiogram.dispatcher.filters import Command
# from aiogram.types import InputFile
# from aiogram.utils import exceptions


#init
# bot = Bot(token=Token.TOKEN)
# dp = Dispatcher(bot)



# -----------------------------------------------------------------------------------
# # PAYMENT SYSTEM
# #price
# PRICE = types.LabeledPrice(label='Підписка на 1 місяць', amount=20000) # це == 20000 / 100 = 200 грн
#
# # buy
# @dp.message_handler(commands=['buy'])
# async def buy(message: types.Message):
#     if Token.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
#         await bot.send_message(message.chat.id, "Тестовий платіж")
#
#     await bot.send_invoice(message.chat.id,
#                            title="Підписка на бота",
#                            description="Активація функціонала бота на 1 місяць",
#                            provider_token=Token.PAYMENTS_TOKEN,
#                            currency='uah',
#                            photo_url='https://blog-assets.lightspeedhq.com/img/2021/06/6f6649f3-payments-101.png',
#                            photo_width=416,
#                            photo_height=234,
#                            photo_size=416,
#                            is_flexible=False,
#                            prices=[PRICE],
#                            start_parameter="one-month-subscription",
#                            payload="test-invoice-payload")
#
# # pre checkout (must be answered in 10 seconds)
# @dp.pre_checkout_query_handler(lambda query: True)
# async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
#     await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)
#
# # successful payment
# @dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
# async def successful_payment(message: types.Message):
#     print("SUCCESSFUL PAYMENT:")
#     payment_info = message.successful_payment.to_python()
#     for key, values in payment_info.items():
#         print(f'{key} = {values}')
#
#     await bot.send_message(message.chat.id,
#                            f"Оплата на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} пройшла успішно")

# -----------------------------------------------------------------------------------

# get_file
# @dp.message_handler(content_types=ContentType.ANY)
# async def get_file(message: types.Message):
#     try:
#         chat_id = message.chat.id
#         file_info = bot.get_file(message.document.file_id)
#         downloaded_file = bot.download_file(file_info.file_path)
#
#         scr = 'D:/Projects/investor_assistant_telegram' + message.document.file_name
#         with open(scr, 'wb') as new_file:
#             new_file.write(downloaded_file)
#
#         await message.answer('File was saved')
#     except Exception:
#         await message.answer('Error')

# -----------------------------------------------------------------------------------


# # get file 2
# async def get_file(message: types.Message):
#     # Check if the user has sent a file
#     if not message.document:
#         await message.reply("Please send me a file.")
#         return
#
#     # Get the file ID and download the file
#     file_id = message.document.file_id
#     file_path = await bot.get_file(file_id).download()
#
#     # Save the file to disk
#     new_file_path = os.path.join("D:\Projects\investor_assistant_telegram", message.document.file_name)
#     os.rename(file_path, new_file_path)
#
#     # Reply to the user
#     await message.reply("File saved.")
# -----------------------------------------------------------------------------------


def register_message_handler():
    dp.message_handler(buy, commands=['buy'])
    dp.pre_checkout_query_handler(pre_checkout_query, lambda query: True)
    dp.message_handler(successful_payment, content_types=ContentType.SUCCESSFUL_PAYMENT)
    dp.register_message_handler(get_file, Command("savefile"))
    # dp.register_message_handler(echo)

if __name__ == '__main__':
    register_message_handler()
    executor.start_polling(dp, skip_updates=False)