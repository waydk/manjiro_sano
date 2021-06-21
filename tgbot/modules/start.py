from aiogram.types import Message
from loguru import logger
from tgbot.utils.db_api import db_helpers


async def start_command(message: Message):
    """
    Responds to /start
    :param message:
    :return:
    """
    user = message.from_user.full_name
    logger.info(f"{user} send /start")
    await message.answer(f"Hello, {user}")
    await db_helpers.add_user(id_user=message.from_user.id, name=user)
