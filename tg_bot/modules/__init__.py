from aiogram import Dispatcher
from aiogram import types

from .antiflood import command_ro, command_un_ro, command_ban, command_un_ban
from .errors import errors_handler
from .start import start_command
from .welcome import welcome_new_member, command_set_welcome
from ..utils.filters import AdminFilter


def setup(dp: Dispatcher):
    dp.register_errors_handler(errors_handler)
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(command_ro, AdminFilter(), commands="ro", commands_prefix='!/')
    dp.register_message_handler(command_un_ro, AdminFilter(), commands="un_ro", commands_prefix='!/')
    dp.register_message_handler(command_ban, AdminFilter(), commands="ban", commands_prefix='!/')
    dp.register_message_handler(command_un_ban, AdminFilter(), commands="un_ban", commands_prefix='!/')
    dp.register_message_handler(welcome_new_member, content_types=types.ContentType.NEW_CHAT_MEMBERS)
    dp.register_message_handler(command_set_welcome, AdminFilter(), commands="set_welcome")
