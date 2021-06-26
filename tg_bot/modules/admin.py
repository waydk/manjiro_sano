import asyncio
import datetime
import re

import aiogram
from aiogram import types
from aiogram.utils.exceptions import BadRequest


async def read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5
    time = int(time)
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)
    try:
        await message.chat.restrict(user_id=member_id, can_send_messages=False, until_date=until_date)
        await message.reply_to_message.delete()
    except aiogram.utils.exceptions.BadRequest as err:
        await message.answer(f"Ошибка! {err.args}")
        return
    await message.answer(f"Пользователю {message.reply_to_message.from_user.full_name} запрещено писать {time} минут.\n"
                         f"По причине: \n<b>{comment}</b>")
    service_message = await message.reply("Сообщение самоуничтожится через 5 секунд.")
    await asyncio.sleep(5)

    await message.delete()
    await service_message.delete()
