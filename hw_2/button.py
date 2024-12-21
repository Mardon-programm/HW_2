from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

MENU = ["Новости", "Курсы валют", "Контактная информация", "Часто задаваемые вопросы - FAQ", "help"]


def genrate_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=menu)] for menu in MENU ],
        resize_keyboard=True
    )
