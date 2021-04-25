import Parse
from loader import dp
from middlewares.message_antiflood import rate_limit
from aiogram import types


@dp.message_handler(commands="cases")
@rate_limit(10)
async def cases(message):
    await message.answer(f'{Parse.cases()} - Total cases')

@dp.callback_query_handler(text='cases')
@rate_limit(10)
async def cases(call: types.CallbackQuery):
    await call.message.answer(f"{Parse.cases()} - Recovered cases.")
    await call.answer()
