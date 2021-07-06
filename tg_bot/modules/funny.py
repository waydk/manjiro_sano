from aiogram import types


async def command_kick(message: types.Message):
    """
    With this command you can kick another user's foot
    """
    try:
        member = message.reply_to_message.from_user
        if member.id == 1869672105:
            await message.answer_animation("https://64.media.tumblr.com/"
                                           "65aa9d26fc3b287a223ddece99bc3220/"
                                           "67181d33d6243f76-f8/s250x400/9af8d1cf18d936d3a2017"
                                           "18d69247694fef26470.gifv",
                                           caption=f"{message.from_user.get_mention(as_html=True)}, "
                                                   f"You're still a long way from me, calm down")
        else:
            await message.answer_animation("https://64.media.tumblr.com/7431fc073f3ed3fa2cf8e5a36fe38317/"
                                           "bfad931b56ede5ff-00/s500x750/cc8727bd7a1b2f874830b4ae599bdde75d7d04c1.gifv")
            await message.answer(f"{message.from_user.get_mention(as_html=True)} kicked "
                                 f"{member.get_mention(as_html=True)} in the face")
    except AttributeError:
        await message.answer("The message must be forwarded to the user you want to "
                             " fuck with your foot!")


async def command_say(message: types.Message):
    """
    With this command you can make the bot write what you want with the gif
    """
    text = message.text.split(" ")[1:]
    if len(text):
        text = ' '.join(text)
    else:
        text = "The main thing in fights is not to win, the main thing is not to lose to yourself"
    await message.answer_animation("https://64.media.tumblr.com/676d0be64ec8f03cc6faadde2c08a56c/"
                                   "67181d33d6243f76-74/s400x600/d95b7e0f8fee31aec3c7062053ffdbe4856a67d7.gifv",
                                   caption=text)
