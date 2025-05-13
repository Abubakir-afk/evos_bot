from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from messages import messages


def start_buttons(lang):
    buttons = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=f"{messages[lang]['about_company']}"),
         KeyboardButton(text=f"{messages[lang]['branches']}")],
        [KeyboardButton(text=f"{messages[lang]['job_positions']}")],
        [KeyboardButton(text=f"{messages[lang]['menu']}"),
         KeyboardButton(text=f"{messages[lang]['news']}")],
        [
            KeyboardButton(text=f"{messages[lang]['contacts']}"),
            KeyboardButton(text=f"{messages[lang]['language']}")
        ],
        [KeyboardButton(text=f"{messages[lang]['send_location']}")]

    ],resize_keyboard=True)

    return buttons

def select_language():
    buttons = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇿", callback_data="uz"),
        InlineKeyboardButton(text="🇷🇺", callback_data="ru"),
         ]

    ], resize_keyboard=True)
    return buttons

def f_buttons(lang):
    btn = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=f"{messages[lang]['Show_nearby_branches']}")],
        [KeyboardButton(text=f"{messages[lang]['head_ofis']}"),
         KeyboardButton(text=f"{messages[lang]['Tashkent.city']}")],
        [KeyboardButton(text=f"{messages[lang]['Back']}")]
    ],resize_keyboard=True)
    return btn

def filial_btn(lang):
    btns = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=f"{messages[lang]['Location']}")],
        [KeyboardButton(text=f"{messages[lang]['back']}")]
    ],resize_keyboard=True)
    return btns

def city_buttons(lang):
    btn = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=f"{messages[lang]['Tashkent']}"),
         KeyboardButton(text=f"{messages[lang]['Andijan']}")],
        [KeyboardButton(text=f"{messages[lang]['Qarshi']}"),
         KeyboardButton(text=f"{messages[lang]['Qoqon']}")],
        [KeyboardButton(text=f"{messages[lang]['Namangan']}"),
         KeyboardButton(text=f"{messages[lang]['Tashkent_region']}")],
        [KeyboardButton(text=f"{messages[lang]['Nukus']}"),
         KeyboardButton(text=f"{messages[lang]['Samarqand']}")],
        [KeyboardButton(text=f"{messages[lang]['Fargona']}"),
         KeyboardButton(text=f"{messages[lang]['Shaxrisabz']}")],
        [KeyboardButton(text=f"{messages[lang]['Xorazim_region']}"),
         KeyboardButton(text=f"{messages[lang]['Navoiy']}")],
        [KeyboardButton(text=f"{messages[lang]['❌Cancel❌']}"),
         KeyboardButton(text=f"{messages[lang]['Back🔙']}")]
    ],resize_keyboard=True)
    return btn