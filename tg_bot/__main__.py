from aiogram import Dispatcher
from loguru import logger

from tg_bot import modules
from tg_bot.utils.db_api.db_gino import db, POSTGRES_URI


async def startup(dispatcher: Dispatcher):
    """Triggers on startup."""

    # Setup handlers
    logger.info("Configuring modules...")
    modules.setup(dispatcher)

    # Working with the database
    logger.info("The database is working...")
    await db.set_bind(POSTGRES_URI)
    await db.gino.create_all()

    # Set command hints
    logger.info("Start polling")
