import Parse
from loader import dp
from middlewares.message_antiflood import rate_limit
from aiogram import types


@dp.message_handler(commands="recovered")
@rate_limit(5)
async def recovered(message):
    await message.answer(f'{Parse.recovered()} - Total recovered')


@dp.callback_query_handler(text='recovered')
@rate_limit(5)
async def recovered(call: types.CallbackQuery):
    await call.message.answer(f"{Parse.recovered()} - Total recovered.")
    await call.answer()
