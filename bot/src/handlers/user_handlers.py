from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from utils import messages
from utils.menus import home_menu, quick_setup_menu


async def send_welcome(message: Message, bot: AsyncTeleBot):
    """
    If user is not active, show setup menu.
    """
    await bot.send_message(message.chat.id, messages.start, reply_markup=quick_setup_menu())


async def home(message: Message, bot: AsyncTeleBot):
    """
    If user is active, show home menu.
    """
    await bot.send_message(message.chat.id, messages.start, reply_markup=home_menu())
