from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from utils import messages
from utils.menus import home_menu, quick_setup_menu


async def send_welcome(message: Message, bot: AsyncTeleBot):
    """
    If user is not active, show setup menu.

    command: /start
    """
    await bot.send_message(message.chat.id, messages.start, reply_markup=quick_setup_menu())

async def quick_setup(message: Message, bot: AsyncTeleBot):
    """
    Setup user service: accounts, members, ...

    Command: `utils.consts.Commands.QUICK_SETUP`
    """
    pass



async def home(message: Message, bot: AsyncTeleBot):
    """
    If user is active, show home menu.

    command: /start
    """
    await bot.send_message(message.chat.id, messages.start, reply_markup=home_menu())
