from aiogram import types
# from bot_launch import bot, dp
# from aiogram.types.message import ContentType


# # get_file                                                      ???
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



# echo
async def echo(message: types.Message):
    await message.answer(f'{message.text}')