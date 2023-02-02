import asyncio
from telebot.async_telebot import AsyncTeleBot

from core.config import settings
from filters import user_filters
from handlers import user_handlers

bot = AsyncTeleBot(settings.API_TOKEN)


def register_handlers():
    bot.register_message_handler(
        user_handlers.send_welcome,
        commands=['start'],
        is_user_active=False,
        pass_bot=True)
    bot.register_message_handler(
        user_handlers.home,
        commands=['start'],
        is_user_active=True,
        pass_bot=True)


register_handlers()

bot.add_custom_filter(user_filters.IsUserDeActive())

async def run():
    await bot.polling(non_stop=True)


asyncio.run(run())
