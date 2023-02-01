
import aiohttp
from telebot.types import Message
from telebot.asyncio_filters import SimpleCustomFilter

class IsUserDeActive(SimpleCustomFilter):
    """
    Check if user is active or not
    """
    key = 'is_user_active'

    async def check(self, message: Message):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://localhost:8000/users/me/status') as resp:
                response = await resp.json()
                user_status = response['is_active']
                print(user_status)
                return user_status