from aiogram import types

import database
from loader import dp
from middlewares.message_antiflood import rate_limit

db = database.DBCommands()


@dp.message_handler(commands=["referrals"])
@rate_limit(5)
async def check_referrals(message: types.Message):
    referrals = await db.check_referrals()
    if referrals != "":
        text = "Your referrals:\n{referrals}".format(referrals=referrals)
        await message.answer(text)
    else:
        await message.answer("You don't have referrals")


@dp.callback_query_handler(text='ref')
@rate_limit(5)
async def general(call: types.CallbackQuery):
    referrals = await db.check_referrals()
    if referrals != '':
        text = "Your referrals:\n{referrals}".format(referrals=referrals)
        await call.message.answer(text)
        await call.answer()
    else:
        await call.message.answer("You don't have referrals")
        await call.answer()
