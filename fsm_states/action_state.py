from aiogram.fsm.state import StatesGroup, State


class FSMActionStates(StatesGroup):
    new_material = State()
    delete_material = State()
    show_own_material = State()
    show_public_material = State()