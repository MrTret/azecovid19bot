import Parse
from loader import dp
from middlewares.message_antiflood import rate_limit
from aiogram import types


@dp.message_handler(commands="deaths")
@rate_limit(5)
async def deaths(message):
    await message.answer(f'{Parse.deaths()} - Total deaths')

@dp.callback_query_handler(text='deaths')
@rate_limit(5)
async def deaths(call: types.CallbackQuery):
    await call.message.answer(f"{Parse.deaths()} - Total deaths.")
    await call.answer()
