from aiogram import Dispatcher

from .errors import errors_handler
from .start import start_command


def setup(dp: Dispatcher):
    dp.register_errors_handler(errors_handler)
    dp.register_message_handler(start_command, commands="start")
