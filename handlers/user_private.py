from aiogram import types, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


from keyboard import reply


user_router = Router()


class ChooseKlass(StatesGroup):
    klass = State()
    liter = State()


@user_router.message(StateFilter(None), F.text == 'Узнать расписание')
async def add_room(message: types.Message, state: FSMContext) -> None:
    await message.answer('Выберите класс, в котором Вы учитесь', reply_markup=reply.choice_klass_kb)
    await state.set_state(ChooseKlass.klass)


@user_router.message(ChooseKlass.klass, F.text)
async def add_room(message: types.Message, state: FSMContext) -> None:
    await state.update_data(klass=message.text)
    await message.answer('Выберите букву', reply_markup=reply.choice_liter_kb)
    await state.set_state(ChooseKlass.liter)


@user_router.message(ChooseKlass.liter, F.text)
async def add_room(message: types.Message, state: FSMContext) -> None:
    await state.update_data(liter=message.text)
    data = await state.get_data()
    try:
        photo = types.FSInputFile(f'timetable/{data.get("klass")}/{data.get("liter")}/timetable.jpg')
        await message.answer_photo(photo=photo, reply_markup=reply.start_kb)
    except:
        await message.answer('К сожалению, не удалось найти расписание.', reply_markup=reply.start_kb)

    await state.clear()
