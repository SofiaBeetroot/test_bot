import pandas as pd
from sqlalchemy import create_engine
import openpyxl
import sqlite3
from config import bot


#get file 2
import os
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile
from aiogram.utils import exceptions

# get file 2
async def get_file(message: types.Message):
    # Check if the user has sent a file
    if not message.document:
        await message.reply("Please send me a file.")

    # Get the file ID and download the file
    file_id = message.document.file_id
    file_path = bot.get_file(file_id).download()
    print(file_path)

    # Save the file to disk
    new_file_path = os.path.join("D:\Projects\investor_assistant_telegram", message.document.file_name)
    os.rename(file_path, new_file_path)

    # Reply to the user
    await message.reply("File saved.")



# # add data from excel to database
# data = pd.read_excel('D:\Projects\investor_assistant_telegram\Netflix-Website-Financials.xlsx', sheet_name="Balance Sheet")
# print(data)


# # connection to database ???
# engine = create_engine('mssql+pyodbc://user:password@server/database?driver=ODBC+Driver+17+for+SQL+Server')

# data = pd.read_excel('D:\Projects\investor_assistant_telegram\Netflix-Website-Financials.xlsx')
# data.to_sql('sqlite_master', con=engine, if_exists='replace', index=False)



# # manipulation with data in database
# conn = sqlite3.connect('database.db')
# cur = conn.cursor()
# cur.execute('SELECT * FROM sqlite_master')
# conn.close()