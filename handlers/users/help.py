from aiogram import types
from aiogram.dispatcher.filters import CommandHelp

from loader import dp
from middlewares.message_antiflood import rate_limit


@dp.message_handler(CommandHelp())
@rate_limit(5)
async def helpcomm(message: types.Message):
    await message.answer("This bot gives you statistics of Covid-19 in Azerbaijan.\n\n\n"
                         "/feedback - if you have errors or ideas send it. Example : /feedback Your bot is very cool."
                         "\n/general - gives you all info."
                         "\n/cases - total cases."
                         "\n/recovered - total recovered."
                         "\n/new - new cases."
                         "\n/active - active cases."
                         "\n/deaths - total deaths."
                         "\n/tests - total tests."
                         "\n/subscribe - subscribes to mailing."
                         "\n/unsubscribe - unsubscribes from mailing.")
