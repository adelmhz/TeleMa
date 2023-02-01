import asyncio
from telebot.async_telebot import AsyncTeleBot

from core.config import settings



bot = AsyncTeleBot(settings.API_TOKEN)

def register_handlers():
    pass

register_handlers()


async def run():
    await bot.polling(non_stop=True)


asyncio.run(run())