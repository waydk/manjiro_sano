from aiogram.types import Message
from loguru import logger
from tg_bot.utils.db_api import db_helpers
from tg_bot.utils.keyboards.main_keyboard import main_markup


async def start_command(message: Message):
    """
    Responds to /start
    :param message:
    :return:
    """
    user = message.from_user.full_name
    logger.info(f"{user} send /start")
    if message.chat.type == 'private':
        await message.answer_photo("https://pbs.twimg.com/media/E036-gkXMAUhG3j?format=jpg&name=large",
                                   caption=f"Hi, {user}. I'm a Telegram bot to manage chats\n"
                                           f"For all questions: @waydk\n"
                                           f"<code>Click the buttons below</code> ",
                                   reply_markup=main_markup)
        await db_helpers.add_user(id_user=message.from_user.id, name=user)
    else:
        await message.answer("Hey, I'm Mikey.")
