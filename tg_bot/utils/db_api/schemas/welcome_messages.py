from sqlalchemy import Column, BigInteger, String, sql

from tg_bot.utils.db_api.db_gino import TimedBaseModel


class WelcomeMessages(TimedBaseModel):
    __tablename__ = 'welcome_messages'
    id_group = Column(BigInteger, primary_key=True)
    message = Column(String(255))
    query: sql.Select
