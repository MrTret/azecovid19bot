from aiogram import types

from loader import dp
from middlewares.message_antiflood import rate_limit


@rate_limit(5)
@dp.callback_query_handler(text='sub')
async def sub(call: types.CallbackQuery):
    await call.answer()


@rate_limit(5)
@dp.message_handler(commands='subscribe')
async def sub(message: types.Message):
    await message.answer("<b>Does not work yet...</b>")


@rate_limit(5)
@dp.callback_query_handler(text='unsub')
async def unsub(call: types.CallbackQuery):
    await call.answer()


@rate_limit(5)
@dp.message_handler(commands='unsubscribe')
async def unsub(message: types.Message):
    await message.answer("<b>Does not work yet...</b>")
