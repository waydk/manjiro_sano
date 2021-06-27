import re
from copy import copy
from datetime import datetime, timedelta

from aiogram import types

default_permissions = {'can_send_messages': True,
                       'can_send_media_messages': True,
                       'can_send_polls': True,
                       'can_send_other_messages': True,
                       'can_add_web_page_previews': True,
                       'can_invite_users': True,
                       'can_change_info': False,
                       'can_pin_messages': False
                       }


def set_user_ro_permissions():
    """
    Assigns permissions
    """
    new_permissions = copy(default_permissions)
    new_permissions.update(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_polls=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_invite_users=False
    )
    return types.ChatPermissions(
        **new_permissions
    )


def parse_duration(duration):
    """
    Splits the admin message into date, comment and time of the mute
    """
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(duration.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5
    time = int(time)
    until_date = datetime.now() + timedelta(minutes=time)
    return until_date, comment, time
