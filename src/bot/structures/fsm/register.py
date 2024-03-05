from aiogram.fsm.state import StatesGroup, State


class RegisterGroup(StatesGroup):
    regFullName = State()
    regPhone = State()


class RegisterMessage(StatesGroup):
    chat_id = State()
    chat_message = State()
