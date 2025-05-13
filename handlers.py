import os

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from database import database
from keyboards import select_language, start_buttons, f_buttons, filial_btn, city_buttons
from messages import messages

router = Router()

@router.message(F.text.in_(["🇺🇿/🇷🇺 Til", "🇺🇿/🇷🇺 Язык"]))
async def get_language(message: Message):
    lang = database.get_user_lang(message.from_user.id)
    await message.answer(messages[lang]['select_lang'], reply_markup=select_language())

@router.callback_query(F.data.in_(["uz", "ru"]))
async def set_language(callback_query: CallbackQuery):
    lang = callback_query.data
    database.set_user_lang(telegram_id=callback_query.from_user.id, lang=lang)
    await callback_query.message.answer(text='Hello', reply_markup=start_buttons(lang))

@router.message(F.text == "🏢 Kampaniya haqida")
async def about_company_handler(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "evos.png"))
    text = ("BIZ HAQIMIZDA!\n"
            "Kompaniyamizning birinchi filiali 2006 yilda ochilgan bo’lib, shu kungacha muvaffaqiyatli faoliyat yuritib "
            "kelmoqdaligini bilarmidingiz? 15 yil davomida kompaniya avtobus bekatidagi kichik ovqatlanish joyidan "
            "zamonaviy, kengaytirilgan tarmoqqa aylandi, u bugungi kunda O‘zbekiston bo‘ylab 65 dan ortiq restoranlarni,"
            "o‘zining eng tezkor yetkazib berish xizmatini, zamonaviy IT-infratuzilmasini va 2000 dan ortiq xodimlarni "
            "o‘z ichiga oladi.")
    await message.answer_photo(photo=img, caption=text)

@router.message(F.text == "📍Filialari")
async def filialari(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img.png"))
    text = ("EVOS - O'zbekistondagi eng yirik fastfud kompaniyasi. Ayni paytda 49 ta chakana savdo shoxobchasi va zamonaviy"
            "diversifikatsiyalangan ishlab chiqarish ochiq. "
            "Kompaniya xodimlari birgalikda rivojlanib, kundan -kunga o'sib "
            "borayotgan katta oila. EVOS har kuni kengayib bormoqda, bugungi kunda bizda bir yarim mingdan ortiq odam bor. Bizning "
            "jamoamizga a'zo bo'ling, EVOS oilasiga xush kelibsiz!")
    lang = database.get_user_lang(message.from_user.id)
    await message.answer_photo(photo=img, caption=text, reply_markup=f_buttons(lang))

@router.message(F.text == "☕️Yaqin filiallarni ko'rsatish")
async def manzil(message: Message):
    text = "Eng yaqin filialni topish uchun joylashuvingizni yuboring!"
    lang = database.get_user_lang(message.from_user.id)
    await message.answer(text=text, reply_markup=filial_btn(lang))

@router.message(F.text == "⬅️Ortga")
async def ortga(message: Message):
    text = "Siz bosh sahifaga qayttingiz!"
    lang = database.get_user_lang(message.from_user.id)
    await message.answer(text=text, reply_markup=start_buttons(lang))

@router.message(F.text == "orqaga")
async def orqaga(message: Message):
    text = "Siz ortga qayttingiz!"
    lang = database.get_user_lang(message.from_user.id)
    await message.answer(text=text, reply_markup=f_buttons(lang))

@router.message(F.text == "👜Bo'sh ish o'rinlari")
async def ish(message: Message):
    text = "📍Shaxarlardan birini tanlang"
    lang = database.get_user_lang(message.from_user.id)
    await message.answer(text=text, reply_markup=city_buttons(lang))