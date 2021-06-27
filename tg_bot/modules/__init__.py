from aiogram import Dispatcher

from .admin import command_ro
from .errors import errors_handler
from .start import start_command
from ..utils.filters import AdminFilter


def setup(dp: Dispatcher):
    dp.register_errors_handler(errors_handler)
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(command_ro, AdminFilter(), commands="ro", commands_prefix='!')
