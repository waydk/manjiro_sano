from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from asyncpg import StringDataRightTruncationError

from tg_bot.utils.db_api import db_helpers


async def welcome_new_member(message: types.Message):
    """
    Welcoming a new persons
    """
    try:
        welcome_message = await db_helpers.select_welcome_message(message.chat.id)
        welcome_message = welcome_message.message
    except AttributeError:
        welcome_message = 'hello'
    for member in message.new_chat_members:
        if member.id == 1834890709:
            username = await message.bot.get_me()
            await message.answer(f"Thank you for adding me to <b>{message.chat.title}</b>\n"
                                 f"I'll help you keep <i>orderly</i> in your group."
                                 f"I'm good at messing with, disrupting, banning and unbanning"
                                 f"But to do that, you have to give the admin to the bot."
                                 f"You can also set your greeting and farewell in the chat."
                                 f"You can get all commands in bot pm",
                                 reply_markup=InlineKeyboardMarkup(
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardButton(text="Go to the bot's PM",
                                                                  url=f"t.me/{username['username']}?start=help")
                                         ]
                                     ]))
        else:
            await message.answer(f"{member.get_mention(as_html=True)}, {welcome_message}")


async def command_set_welcome(message: types.Message):
    """
    Set welcome text
    """
    if len(message.text.split(' ')) == 1:
        await message.answer('try: /set_welcome "some text"')
        return
    welcome_text = ' '.join(message.text.split(' ')[1:])
    try:
        await db_helpers.add_welcome_message(id_group=message.chat.id, message=welcome_text)
    except StringDataRightTruncationError:
        await message.answer("The maximum length is 255 characters, try another text ")
        return
    await message.answer(f"Your welcome text - {welcome_text}\n"
                         f"<code>INSTALLED</code>")
