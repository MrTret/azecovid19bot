from aiogram import types

from loader import dp, bot
from middlewares.message_antiflood import rate_limit


@dp.message_handler(commands='feedback')
@rate_limit(5)
async def feedback(message: types.Message):
    if message.get_args() != "":
        await bot.send_message(-559169340, f"[SENT BY] : <a href='tg://user?id={message.from_user.id}'>{message.from_user.id}</a>"
                                           f"\n[MESSAGE] : {message.get_args()}")
        await message.reply(f"""<b>Thank you for feedback, <a href="tg://user?id={message.from_user.id}">dear User!</a></b>""")
    else:
        await message.reply("<i>Message shouldn't be empty!</i>"
                            "\n<i>For Example : /feedback cool bot!</i>")
