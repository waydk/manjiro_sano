from aiogram import types


async def welcome_new_member(message: types.Message):
    for member in message.new_chat_members:
        if member.id == 1869672105:
            await message.answer('Thank you for adding me to the group')
        else:
            await message.answer(f"{member.get_mention(as_html=True)}, hi")



