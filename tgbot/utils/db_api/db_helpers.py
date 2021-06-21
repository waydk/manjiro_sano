from asyncpg import UniqueViolationError

from tgbot.utils.db_api.schemas.user import User


async def add_user(id_user: int, name: str):
    """
    Adds a user to the database
    :param id_user:
    :param name:
    :return:
    """
    try:
        user = User(id=id_user, name=name)
        await user.create()

    except UniqueViolationError:
        pass


