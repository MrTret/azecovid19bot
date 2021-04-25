import Parse
from loader import dp
from middlewares.message_antiflood import rate_limit
from aiogram import types


@dp.message_handler(commands='summary')
@rate_limit(5)
async def general(message: types.Message):
    await message.answer("<b>Does not work yet...</b>")


@dp.callback_query_handler(text='general')
@rate_limit(5)
async def general(call: types.CallbackQuery):
    await call.message.answer("<b>Does not work yet...</b>")
    await call.answer()