from aiogram import types

import database
from config import ADMINS
from loader import dp

db = database.DBCommands()


@dp.message_handler(commands='ahelp', chat_id=ADMINS)
async def adminhelp(message: types.Message):
    await message.answer("/ref"
                         "\n/users")


@dp.message_handler(commands='ref', chat_id=ADMINS)
async def adminrefs(message: types.Message):
    try:
        referrals = await db.admin_check_referrals(message=message)

        if referrals != "":
            text = "Your referrals:\n{referrals}".format(referrals=referrals)
            await message.answer(text)
        else:
            await message.answer("User does not have referrals")
    except Exception:
        await message.answer('/ref id')


@dp.message_handler(commands='users', chat_id=ADMINS)
async def adminusers(message: types.Message):
    users = await db.admin_check_users()

    text = "{users}".format(users=users)
    await message.answer(text, parse_mode="")
