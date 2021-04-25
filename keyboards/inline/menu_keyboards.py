# from wand.image import Image
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


menu_list = CallbackData("level", "list")


def make_callback_data(list):
    return menu_list.new(list=list)


async def keyboard():
    current = 0
    markup = InlineKeyboardMarkup(row_width=2)
    item1 = InlineKeyboardButton('Cases', callback_data='cases')
    item2 = InlineKeyboardButton('Recovered', callback_data='recovered')
    item3 = InlineKeyboardButton('New Cases', callback_data='new')
    item4 = InlineKeyboardButton('Active Cases', callback_data='active')
    item5 = InlineKeyboardButton('Deaths', callback_data='deaths')
    item6 = InlineKeyboardButton('Tests', callback_data='tests')
    item7 = InlineKeyboardButton('Summary🖼️', callback_data='general')
    markup = markup.add(item1, item2, item3, item4, item5, item6, item7)

    markup.row(
        InlineKeyboardButton(
            text="▶",
            callback_data=make_callback_data(list=current + 1)
        )
    )

    return markup


async def keyboard2():
    current = 1
    markup = InlineKeyboardMarkup(row_width=3)
    item1 = InlineKeyboardButton('Referrals', callback_data='ref')
    item2 = InlineKeyboardButton('---', callback_data='sub')
    item3 = InlineKeyboardButton('---', callback_data='unsub')

    markup = markup.add(item1)
    markup.row(item2, item3)

    markup.row(
        InlineKeyboardButton(
            text="◀",
            callback_data=make_callback_data(list=current - 1)
        )
    )

    return markup
