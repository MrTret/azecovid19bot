from aiogram import  Dispatcher

from loader import dp
from .message_antiflood import ThrottlingMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
