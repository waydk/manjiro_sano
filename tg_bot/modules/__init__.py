from aiogram import Dispatcher
from aiogram import types

from .anime import anime_info
from .antiflood import command_mute, command_un_mute, command_ban, command_un_ban
from .errors import errors_handler
from .farewell import farewell_left_member, command_set_farewell
from .funny import command_kick, command_say
from .help import command_help, show_info_anime, back_to_help, show_anti_flood_info, show_funny_info, show_help, \
    show_service_info, back_to_start
from .start import start_command
from .welcome import welcome_new_member, command_set_welcome
from ..utils.filters import AdminFilter
from ..utils.keyboards.main_keyboard import help_callback


def setup(dp: Dispatcher):
    dp.register_errors_handler(errors_handler)
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(command_help, commands="help")
    dp.register_message_handler(command_mute, AdminFilter(), commands="mute", commands_prefix='!/')
    dp.register_message_handler(command_un_mute, AdminFilter(), commands="unmute", commands_prefix='!/')
    dp.register_message_handler(command_ban, AdminFilter(), commands="ban", commands_prefix='!/')
    dp.register_message_handler(command_un_ban, AdminFilter(), commands="unban", commands_prefix='!/')
    dp.register_message_handler(welcome_new_member, content_types=types.ContentType.NEW_CHAT_MEMBERS)
    dp.register_message_handler(command_set_welcome, AdminFilter(), commands="set_welcome")
    dp.register_message_handler(farewell_left_member, content_types=types.ContentType.LEFT_CHAT_MEMBER)
    dp.register_message_handler(command_set_farewell, AdminFilter(), commands="set_farewell")
    dp.register_message_handler(command_kick, commands="kick")
    dp.register_message_handler(anime_info, commands="anime")
    dp.register_message_handler(command_say, commands="say")
    dp.register_callback_query_handler(show_info_anime, help_callback.filter(name="anime_info"))
    dp.register_callback_query_handler(back_to_help, help_callback.filter(name='back'))
    dp.register_callback_query_handler(show_anti_flood_info, help_callback.filter(name="antiflood_info"))
    dp.register_callback_query_handler(show_funny_info, help_callback.filter(name="fan_info"))
    dp.register_callback_query_handler(show_help, help_callback.filter(name="show_info"))
    dp.register_callback_query_handler(show_service_info, help_callback.filter(name="service"))
    dp.register_callback_query_handler(back_to_start, help_callback.filter(name='back_start'))
