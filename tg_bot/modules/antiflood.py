import asyncio

import aiogram
from aiogram import types
from aiogram.utils.exceptions import BadRequest

from tg_bot.utils.admin_helpers import parse_duration, set_user_ro_permissions


async def command_ro(message: types.Message):
    """
    Command restricting the user
    """
    try:
        member = message.reply_to_message.from_user
    except AttributeError:
        await message.answer("<b>The message must be forwarded!</b>")
        return
    until_date, reason, time = parse_duration(message)
    try:
        await message.chat.restrict(user_id=member.id, permissions=set_user_ro_permissions(),
                                    until_date=until_date)
        await message.reply_to_message.delete()
    except aiogram.utils.exceptions.BadRequest as err:
        await message.answer(f"Error! - <code>{err.args}</code>")
        return
    await message.answer(f"User  <code>{member.full_name}</code>  received a mute on account of  <code>{reason}</code>"
                         f"  for  <code>{time}</code>  minutes")
    service_message = await message.reply("5 secs")
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()
