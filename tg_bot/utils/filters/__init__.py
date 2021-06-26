from aiogram import Dispatcher

from tg_bot.utils.filters.admins import AdminFilter


def setup(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)
