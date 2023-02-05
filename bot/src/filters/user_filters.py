
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from telebot.asyncio_filters import SimpleCustomFilter

from utils.api_helpers import get_user_status


class IsUserActive(SimpleCustomFilter):
    """
    Check if user is active or not
    """
    key = 'is_user_active'

    async def check(self, message: Message):
        chat_id = str(message.chat.id)
        user_status = await get_user_status(chat_id=chat_id)
        return user_status

def bind_filters(bot: AsyncTeleBot):
    bot.add_custom_filter(IsUserActive())