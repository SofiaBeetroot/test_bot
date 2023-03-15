from aiogram.dispatcher.filters.state import StatesGroup, State


class FileState(StatesGroup):
    waiting_for_file = State()
