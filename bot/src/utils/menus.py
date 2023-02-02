from telebot import types

from .consts import Commands

def home_menu():
    markup = types.ReplyKeyboardMarkup()
    quick_setup = types.KeyboardButton(Commands.QUICK_SETUP)
    send = types.KeyboardButton(Commands.SEND)
    add = types.KeyboardButton(Commands.ADD)
    show_unread_messages = types.KeyboardButton(Commands.SHOW_UNREAD_MESSAGES)
    setting = types.KeyboardButton(Commands.SETTING)
    report = types.KeyboardButton(Commands.REPORT)
    accounts = types.KeyboardButton(Commands.ACCOUNTS)
    members = types.KeyboardButton(Commands.MEMBERS)
    support = types.KeyboardButton(Commands.SUPPORT)

    markup.row(quick_setup)
    markup.row(send, add)
    markup.row(show_unread_messages)
    markup.row(setting, report)
    markup.row(accounts, members)
    markup.row(support)

    return markup

def quick_setup_menu():
    markup = types.ReplyKeyboardMarkup()
    quick_setup = types.KeyboardButton(Commands.QUICK_SETUP)
    markup.row(quick_setup)

    return markup
