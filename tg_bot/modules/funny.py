from aiogram import types


async def command_kick(message: types.Message):
    try:
        member = message.reply_to_message.from_user
        if member.id == 1869672105:
            await message.answer_photo("https://i.pinimg.com/564x/62/21/f9/6221f986da15fede0ac97048f8fbb65a.jpg",
                                       caption='You have yet to grow up to me.')
        else:
            await message.answer(f"{message.from_user.get_mention(as_html=True)} kicked "
                                 f"{member.get_mention(as_html=True)} with his foot")
    except AttributeError:
        await message.answer("<b>The message must be forwarded!</b>")
