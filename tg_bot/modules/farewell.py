from aiogram import types
from asyncpg import StringDataRightTruncationError

from tg_bot.utils.db_api import db_helpers


async def farewell_left_member(message: types.Message):
    """
    Saying goodbye to the departed
    """
    try:
        farewell_message = await db_helpers.select_farewell_message(message.chat.id)
        farewell_message = farewell_message.message
    except AttributeError:
        farewell_message = 'Goodbye, man 😔'
    await message.answer(f"{message.left_chat_member.get_mention(as_html=True)}, {farewell_message}")


async def command_set_farewell(message: types.Message):
    """
    Set farewell text
    """
    if len(message.text.split(' ')) == 1:
        await message.answer('try: /set_farewell "some text"')
        return
    farewell_text = ' '.join(message.text.split(' ')[1:])
    try:
        await db_helpers.add_farewell_message(id_group=message.chat.id, message=farewell_text)
    except StringDataRightTruncationError:
        await message.answer("The maximum length is 255 characters, try another text")
        return
    await message.answer(f"Your farewell text - {farewell_text}\n"
                         f"<code>INSTALLED</code>")
