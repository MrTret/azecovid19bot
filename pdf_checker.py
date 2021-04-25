from apscheduler.schedulers.asyncio import AsyncIOScheduler

from database import skt
import asyncio
import database
import get_pdf
from database import Covid19
from loader import bot

db = database.DBCommands()
scheduler = AsyncIOScheduler()


# async def sender():
#     if db.last():
#         get_pdf.download()
#         get_pdf.convert()
#         users = await User.query.where(User.subscription == 1).gino.all()
#         doc = open('covid19.jpg', 'rb')
#         msg = await bot.send_photo(818947432, doc)
# await Covid19.create(Covid19.file_id == msg)
# else:
#     pass
# await sender()
# for user in users:
#     try:
# doc = open('covid19.jpg', 'rb')
# await bot.send_message(chat_id=user.user_id, doc)
#
# await sleep(0.3)
# except Exception:
#     pass
# finally:
