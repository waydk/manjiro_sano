import asyncio

import aiogram
from aiogram import types
from aiogram.utils.exceptions import BadRequest

from tg_bot.utils.admin_helpers import parse_duration, set_un_ro_permissions, set_ro_permissions


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
        await message.chat.restrict(user_id=member.id, permissions=set_ro_permissions(),
                                    until_date=until_date)
    except aiogram.utils.exceptions.BadRequest as err:
        await message.answer(f"<code>{err.args[0]}</code>")
        return
    await message.answer(f"User  <code>{member.full_name}</code>  received a mute on account of  <code>{reason}</code>"
                         f"  for  <code>{time}</code>  minutes")
    service_message = await message.reply("The message will be deleted after 5 seconds")

    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()


async def command_un_ro(message: types.Message):
    """
    A command that removes restrictions from the user
    """
    try:
        member = message.reply_to_message.from_user
    except AttributeError:
        await message.answer("<b>The message must be forwarded!</b>")
        return
    try:
        await message.chat.restrict(user_id=member.id, permissions=set_un_ro_permissions(), )
        await message.answer(f"<code>{member.full_name}</code> was taken off the mute!")
    except aiogram.utils.exceptions.BadRequest as err:
        await message.answer(f"<code>{err.args[0]}</code>")
        return


async def command_ban(message: types.Message):
    """
    The command allows you to ban a user
    """
    try:
        member = message.reply_to_message.from_user
    except AttributeError:
        await message.answer("<b>The message must be forwarded!</b>")
        return
    try:
        await message.chat.kick(user_id=member.id)
    except BadRequest:
        await message.answer(f"User <code>{member.full_name}</code> - admin")
        return
    await message.answer(f"User <code>{member.full_name}</code> banned!")

    service_message = await message.answer("The message will be deleted after 5 seconds.")
    await asyncio.sleep(5)
    await message.reply_to_message.delete()
    await message.delete()
    await service_message.delete()


async def command_un_ban(message: types.Message):
    """
    The command allows you to unban a user
    """
    try:
        member = message.reply_to_message.from_user
    except AttributeError:
        await message.answer("<b>The message must be forwarded!</b>")
        return
    await message.chat.unban(user_id=member.id)
    await message.answer(f"<code>{member.full_name}</code> unbanned")
