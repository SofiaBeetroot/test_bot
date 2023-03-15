from aiogram.dispatcher import FSMContext
from config import bot
import os
from aiogram import types
from handlers.auto_state import FileState

async def get_file(message: types.Message):
    # Check if the user has sent a file
    await FileState.waiting_for_file.set()

    await message.reply("Please send me a file.")

async def read_file(message: types.Message, state: FSMContext):
    # Get the file ID and download the file
    print('Here')
    file_id = message.document.file_id
    print(file_id)
    file_path = bot.get_file(file_id).download()
    print(file_path)

    async with state.proxy() as data:
        data['waiting_for_file'] = file_path

    # Save the file to disk
    new_file_path = os.path.join("D:\Projects\investor_assistant_telegram", message.document.file_name)
    os.rename(file_path, new_file_path)

    # Reply to the user
    await message.reply("File saved.")
    await state.finish()