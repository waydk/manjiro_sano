from sqlalchemy import Column, BigInteger, String, sql

from tg_bot.utils.db_api.db_gino import TimedBaseModel


class FarewellMessages(TimedBaseModel):
    __tablename__ = 'farewell_messages'
    id_group = Column(BigInteger, primary_key=True)
    message = Column(String(255))
    query: sql.Select
