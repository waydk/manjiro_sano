from aiogram import Dispatcher

from .antiflood import command_ro, command_un_ro, command_ban, command_un_ban
from .errors import errors_handler
from .start import start_command
from ..utils.filters import AdminFilter


def setup(dp: Dispatcher):
    dp.register_errors_handler(errors_handler)
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(command_ro, AdminFilter(), commands="ro", commands_prefix='!/')
    dp.register_message_handler(command_un_ro, AdminFilter(), commands="un_ro", commands_prefix='!/')
    dp.register_message_handler(command_ban, AdminFilter(), commands="ban", commands_prefix='!/')
    dp.register_message_handler(command_un_ban, AdminFilter(), commands="un_ban", commands_prefix='!/')
