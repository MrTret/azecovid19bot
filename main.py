import logging
from aiogram import executor

from config import ADMINS
from loader import dp, bot
from database import create_db


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def on_startup(dp):
    await create_db()
    for admins in ADMINS:
        await bot.send_message(chat_id=admins, text="Bot is up!"
                                                    "\n/ref id"
                                                    "\n/users")


if __name__ == "__main__":
    from handlers import dp
    # Запуск бота
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
