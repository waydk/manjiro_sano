import asyncio

from aiogram import types
from aiogram.utils.exceptions import CantRestrictSelf, UserIsAnAdministratorOfTheChat, \
    NotEnoughRightsToRestrict
from loguru import logger

from tg_bot.utils.admin_helpers import parse_duration, set_un_ro_permissions, set_ro_permissions


async def get_member(message, command, example):
    """
    getting the user from reply message
    """
    try:
        member = message.reply_to_message.from_user
        logger.info(f"received the user {member}")
    except AttributeError:
        await message.answer(f"You must <b>send</b> the message "
                             f"user\nwith command <code>{command}</code>\n"
                             f"{example}")
        return
    return member


async def processing(member, message, until_date, command, permissions):
    try:
        logger.info(f"{member} got a {command}")
        if command == 'mute':
            await message.chat.restrict(user_id=member.id, permissions=permissions,
                                        until_date=until_date)
        elif command == 'ban':
            await message.chat.kick(user_id=member.id)
        elif command == 'unban':
            await message.chat.unban(user_id=member.id)
        else:
            await message.chat.restrict(user_id=member.id, permissions=permissions)
    except AttributeError:
        return False
    except CantRestrictSelf:
        await message.answer(f"It's impossible to restrict yourself")
        return False
    except UserIsAnAdministratorOfTheChat:
        await message.answer(f"{member.get_mention(as_html=True)} is an administrator")
        return False
    except NotEnoughRightsToRestrict:
        await message.answer("I'm not an admin!!!!")
        return False
    return True


async def command_mute(message: types.Message):
    """
    command restricting the user
    """
    member = await get_member(message, "!mute или /mute",
                              example="Example: <code>!mute 1 spam</code>")
    until_date, reason, time = parse_duration(message)
    if not await processing(
            member,
            message,
            until_date,
            command="mute",
            permissions=set_ro_permissions()):
        return
    await message.answer(f"{member.get_mention(as_html=True)} received a mute for the reason: <code>{reason}</code>"
                         f"  for  <code>{time}</code> minute/minutes")
    service_message = await message.reply("The message will be deleted after 5 secs")
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()


async def command_un_mute(message: types.Message):
    """
    command that removes restrictions from the user
    """
    member = await get_member(message, "!unmute или /unmute",
                              example="Example: /unmute")
    if not await processing(member,
                            message,
                            until_date=None,
                            command="unmute",
                            permissions=set_un_ro_permissions()):
        return
    await message.answer(f"{member.get_mention(as_html=True)} was unmuted and can now write in the chat again")


async def command_ban(message: types.Message):
    """
    command allows you to ban a user
    """
    member = await get_member(message, command='!ban или /ban',
                              example="Example: /ban")

    if not await processing(member, message, until_date=False, command="ban",
                            permissions=False):
        return

    await message.chat.kick(user_id=member.id)

    await message.answer(f"{member.get_mention(as_html=True)} was banned! goodbye 😔")

    service_message = await message.answer("The message will be deleted after 5 secs")
    await asyncio.sleep(5)
    await message.reply_to_message.delete()
    await message.delete()
    await service_message.delete()


async def command_un_ban(message: types.Message):
    """
    command allows you to unban a user
    """
    member = await get_member(message, "!unban или /unban",
                              example="Example: /unban")
    if not await processing(member, message, until_date=False, command='unban',
                            permissions=False):
        return

    await message.answer(f"{member.get_mention(as_html=True)} has been unbanished")
