import Parse
from loader import dp
from middlewares.message_antiflood import rate_limit
from aiogram import types


@dp.message_handler(commands="active")
@rate_limit(10)
async def active(message):
    await message.answer(f'{Parse.active()} - Active cases')


@dp.callback_query_handler(text='active')
@rate_limit(10)
async def active(call: types.CallbackQuery):
    await call.message.answer(f"{Parse.active()} - Active cases.")
    await call.answer()
