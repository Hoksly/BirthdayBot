import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot is working")

        except Exception as err:
            logging.exception(err)


async def on_end_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot has been stopped")

        except Exception as err:
            logging.exception(err)
