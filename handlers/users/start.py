from aiogram.dispatcher.filters import CommandStart

from keyboards.inline.menu_keyboards import keyboard, keyboard2, menu_list
from loader import dp
from middlewares.message_antiflood import rate_limit
from aiogram import types

import database

db = database.DBCommands()


@dp.message_handler(CommandStart())
@rate_limit(5)
async def register(message: [types.Message, types.CallbackQuery], **kwargs):
    markup = await keyboard()

    if isinstance(message, types.Message):
        referral = message.get_args()
        user = await db.add_new_user(referral=referral)
        id = user.id
        count_users = await db.count_users()
        bot_link = f"https://t.me/azecovid19bot?start={id}"
        text = ("Hi, this bot gives you statistics of Covid-19 in Azerbaijan!\n"
                "{count_users} users use this bot!\n\n"
                "Your referral link: {bot_link}\n").format(
            count_users=count_users,
            bot_link=bot_link
        )
        await message.answer(text=text, reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)
        await call.answer()


async def welcome2(callback: types.CallbackQuery, **kwargs):
    markup = await keyboard2()
    await callback.message.edit_reply_markup(markup)
    await callback.answer()


@dp.callback_query_handler(menu_list.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get("list")

    levels = {
        "0": register,
        "1": welcome2,
    }

    current_level_function = levels[current_level]

    await current_level_function(
        call,
        list=list
    )
