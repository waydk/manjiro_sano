from asyncpg import UniqueViolationError

from tg_bot.utils.db_api.schemas.farewell_messages import FarewellMessages
from tg_bot.utils.db_api.schemas.user import User
from tg_bot.utils.db_api.schemas.welcome_messages import WelcomeMessages


async def add_user(id_user: int, name: str):
    """
    Adds a user to the database
    """
    try:
        user = User(id=id_user, name=name)
        await user.create()

    except UniqueViolationError:
        pass


async def add_welcome_message(id_group: int, message: str):
    """
    add welcome messages to database
    """
    welcome_message = WelcomeMessages(id_group=id_group, message=message)
    try:
        await welcome_message.create()
    except UniqueViolationError:
        await welcome_message.update(message=message).apply()


async def add_farewell_message(id_group: int, message: str):
    """
    add farewell messages to database
    """
    farewell_message = FarewellMessages(id_group=id_group, message=message)
    try:
        await farewell_message.create()
    except UniqueViolationError:
        await farewell_message.update(message=message).apply()


async def select_welcome_message(id_group: int):
    """
    get welcome messages from database
    """
    welcome_message = await WelcomeMessages.query.where(WelcomeMessages.id_group == id_group).gino.first()
    return welcome_message


async def select_farewell_message(id_group: int):
    """
    get farewell messages from database
    """
    farewell_message = await FarewellMessages.query.where(FarewellMessages.id_group == id_group).gino.first()
    return farewell_message
