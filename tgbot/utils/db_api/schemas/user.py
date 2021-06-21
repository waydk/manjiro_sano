from sqlalchemy import Column, BigInteger, String, sql

from tgbot.utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'test'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    query: sql.Select
