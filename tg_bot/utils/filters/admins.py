from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message


class AdminFilter(BoundFilter):
    async def check(self, message: Message) -> bool:
        member = await message.chat.get_member(message.from_user.id)
        return member.is_chat_admin()
