from aiogram import types, Bot
from gino import Gino
from gino.schema import GinoSchemaVisitor
from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence, TIMESTAMP, Boolean)
from sqlalchemy import sql

from config import DB_PASS, DB_USER, host
from get_pdf import pdf

db = Gino()


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger)
    full_name = Column(String(100))
    username = Column(String(50))
    referral = Column(Integer)
    subscription = Column(Boolean, default=True)
    query: sql.Select

    def __repr__(self):
        return "<User(id='{}', fullname='{}', username='{}', user_id='{}')>".format(
            self.id, self.full_name, self.username, self.user_id)


class Covid19(db.Model):
    __tablename__ = 'covid19'

    link = Column(String(250))
    file_id = Column(String(200))
    query: sql.Select

    def __repr__(self):
        return "<Covid(link='{}', file_id='{}')>".format(
            self.link, self.file_id)


class DBCommands:
    async def get_user(self, user_id):
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user

    async def add_new_user(self, referral=None):
        user = types.User.get_current()
        old_user = await self.get_user(user.id)
        if old_user:
            return old_user
        new_user = User()
        new_user.user_id = user.id
        new_user.username = user.username
        new_user.full_name = user.full_name

        if referral:
            new_user.referral = int(referral)
        await new_user.create()
        return new_user

    # async def last(self):
    #     last = await Covid19.query.order_by(Covid19.link.desc()).gino.first()
        # if pdf() != last:
        #     new_link = Covid19()
        #     new_link.link = pdf()
        #     await new_link.create()
        #     print(last)
        #     await last()
        # else:
        #     return False
        # print(last)

    async def count_users(self) -> int:
        total = await db.func.count(User.id).gino.scalar()
        return total

    async def check_referrals(self):
        bot = Bot.get_current()
        user_id = types.User.get_current().id

        user = await User.query.where(User.user_id == user_id).gino.first()
        referrals = await User.query.where(User.referral == user.id).gino.all()

        return ", ".join([
            f"{num + 1}. " + (await bot.get_chat(referral.user_id)).get_mention(as_html=True)
            for num, referral in enumerate(referrals)
        ])

    async def admin_check_referrals(self, message):
        bot = Bot.get_current()
        id = int(message.get_args())

        user = await User.query.where(User.id == id).gino.first()
        referrals = await User.query.where(User.referral == id).gino.all()
        print(user)
        return ", ".join([
            f"{num + 1}. " + (await bot.get_chat(referral.user_id)).get_mention(as_html=True)
            for num, referral in enumerate(referrals)
        ])

    async def admin_check_users(self):
        user = await User.query.gino.all()
        return user

async def skt():
    last = Covid19.query.order_by(Covid19.link.desc()).gino.first()
    print(last)

async def create_db():
    await db.set_bind(f'postgresql://{DB_USER}:{DB_PASS}@{host}/gino')
    db.gino: GinoSchemaVisitor
    await db.gino.create_all()
