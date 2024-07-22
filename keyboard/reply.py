from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Узнать расписание')
        ]
    ],
    resize_keyboard=True
)

choice_klass_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='5'),
            KeyboardButton(text='6'),
            KeyboardButton(text='7'),
            KeyboardButton(text='8')
        ],

        [
            KeyboardButton(text='9'),
            KeyboardButton(text='10'),
            KeyboardButton(text='11')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите класс'
)


choice_liter_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='А'),
            KeyboardButton(text='Б'),
            KeyboardButton(text='В'),
        ],
        [
            KeyboardButton(text='Г'),
            KeyboardButton(text='Д'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите букву'
)

del_keyboard = ReplyKeyboardRemove()
