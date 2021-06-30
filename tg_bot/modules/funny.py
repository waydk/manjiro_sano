from aiogram import types
from aiogram.utils.exceptions import MessageTextIsEmpty


async def command_kick(message: types.Message):
    """
    With this command you can kick another user's foot
    """
    try:
        member = message.reply_to_message.from_user
        if member.id == 1869672105:
            await message.answer_photo("https://i.pinimg.com/564x/62/21/f9/6221f986da15fede0ac97048f8fbb65a.jpg",
                                       caption='You have yet to grow up to me.')
        else:
            await message.answer_animation("https://64.media.tumblr.com/7431fc073f3ed3fa2cf8e5a36fe38317/"
                                           "bfad931b56ede5ff-00/s500x750/cc8727bd7a1b2f874830b4ae599bdde75d7d04c1.gifv")
            await message.answer(f"{message.from_user.get_mention(as_html=True)} kicked "
                                 f"{member.get_mention(as_html=True)} with his foot")
    except AttributeError:
        await message.answer("<b>The message must be forwarded!</b>")


async def command_say(message: types.Message):
    """
    With this command you can make the bot write what you want with the gif
    """
    try:
        text = message.text.split(" ")[1:]
        await message.answer_animation("https://64.media.tumblr.com/676d0be64ec8f03cc6faadde2c08a56c/"
                                       "67181d33d6243f76-74/s400x600/d95b7e0f8fee31aec3c7062053ffdbe4856a67d7.gifv")
        await message.answer(' '.join(text))
    except MessageTextIsEmpty:
        await message.answer("Toman belongs to me. As long as I’m standing in the background, no one can lose.")
