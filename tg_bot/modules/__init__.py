from aiogram import Dispatcher
from aiogram import types

from .anime import anime_info
from .antiflood import command_mute, command_un_mute, command_ban, command_un_ban
from .errors import errors_handler
from .farewell import farewell_left_member, command_set_farewell
from .funny import command_kick, command_say
from .start import start_command
from .welcome import welcome_new_member, command_set_welcome
from ..utils.filters import AdminFilter


def setup(dp: Dispatcher):
    dp.register_errors_handler(errors_handler)
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(command_mute, AdminFilter(), commands="mute", commands_prefix='!/')
    dp.register_message_handler(command_un_mute, AdminFilter(), commands="unmute", commands_prefix='!/')
    dp.register_message_handler(command_ban, AdminFilter(), commands="ban", commands_prefix='!/')
    dp.register_message_handler(command_un_ban, AdminFilter(), commands="un_ban", commands_prefix='!/')
    dp.register_message_handler(welcome_new_member, content_types=types.ContentType.NEW_CHAT_MEMBERS)
    dp.register_message_handler(command_set_welcome, AdminFilter(), commands="set_welcome")
    dp.register_message_handler(farewell_left_member, content_types=types.ContentType.LEFT_CHAT_MEMBER)
    dp.register_message_handler(command_set_farewell, AdminFilter(), commands="set_farewell")
    dp.register_message_handler(command_kick, commands="kick")
    dp.register_message_handler(anime_info, commands="anime")
    dp.register_message_handler(command_say, commands="say")
