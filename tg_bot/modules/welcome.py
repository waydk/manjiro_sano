from aiogram import types

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
        if member.id == 1869672105:
            await message.answer('Thank you for adding me to the group')
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
    print(welcome_text)
    await db_helpers.add_welcome_message(id_group=message.chat.id, message=welcome_text)
    await message.answer(f"your welcome text is set - {welcome_text}")
