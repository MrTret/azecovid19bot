import Parse
from loader import dp
from middlewares.message_antiflood import rate_limit
from aiogram import types


@dp.message_handler(commands="tests")
@rate_limit(5)
async def tests(message):
    await message.answer(f'{Parse.tests()} - Total tests')


@dp.callback_query_handler(text='tests')
@rate_limit(5)
async def tests(call: types.CallbackQuery):
    await call.message.answer(f"{Parse.tests()} - Total tests.")
    await call.answer()
