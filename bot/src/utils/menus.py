from telebot import types

def home_menu():
    markup = types.ReplyKeyboardMarkup()
    quick_setup = types.KeyboardButton('👤Quick setup')
    send = types.KeyboardButton('📤Send')
    add = types.KeyboardButton('📲Add')
    show_unread_messages = types.KeyboardButton('👁‍🗨Show unread messages')
    setting = types.KeyboardButton('⚙️Setting')
    report = types.KeyboardButton('📃Report')
    accounts = types.KeyboardButton('Accounts')
    members = types.KeyboardButton('Members')
    support = types.KeyboardButton('⁉️Support/help')

    markup.row(quick_setup)
    markup.row(send, add)
    markup.row(show_unread_messages)
    markup.row(setting, report)
    markup.row(accounts, members)
    markup.row(support)

    return markup

def quick_setup_menu():
    markup = types.ReplyKeyboardMarkup()
    quick_setup = types.KeyboardButton('Quick setup')
    markup.row(quick_setup)

    return markup
