from aiogram import types

import Parse
from loader import dp
from middlewares.message_antiflood import rate_limit


@dp.message_handler(commands="new")
@rate_limit(5)
async def new(message):
    await message.answer(f'{Parse.new()} - New cases')


@dp.callback_query_handler(text='new')
@rate_limit(5)
async def new(call: types.CallbackQuery):
    await call.message.answer(f"{Parse.new()} - New cases.")
    await call.answer()
