import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from config import TOKEN

from keyboard import reply
from handlers.user_private import user_router


token = TOKEN
dp = Dispatcher()
dp.include_router(user_router)


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f'Здравствуйте, {message.from_user.first_name}!\n'
                         f'\n'
                         f'Я помогу тебе узнать расписание уроков.\n',
                         reply_markup=reply.start_kb)


async def main():
    bot = Bot(token)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
