from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode

from language import LanguageManager, Language, Context

import asyncio

TOKEN = "7909102868:AAFfdT5llQ7m8DSo-oFsG6XMXGLBGAqGExY"

dp = Dispatcher()
router = Router()

# Store per-user language preference
user_languages: dict[int, Language] = {}

@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id
    language_code = message.from_user.language_code.upper() if message.from_user.language_code else "EN"

    if LanguageManager().has_language(language_code):
        user_languages[user_id] = Language[language_code]
        await message.answer(LanguageManager().get_phrase(Context.WELCOME), parse_mode=ParseMode.HTML)

    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Yes, English is fine", callback_data="language_english"),
                InlineKeyboardButton(text="🌐 No, change language", callback_data="change_language")
            ]
        ])
        await message.answer(
            "Sorry, <b>I don't have your language</b> that you are working with :/\nCould we continue English?",
            parse_mode=ParseMode.HTML,
            reply_markup=keyboard
        )
        # Default to English until they choose
        user_languages[user_id] = Language.EN

@router.callback_query(F.data == "language_english")
async def handle_language_english(callback: CallbackQuery):
    user_id = callback.from_user.id
    user_languages[user_id] = Language.EN
    await callback.message.answer("Great! We'll continue in English. 🇬🇧")
    await callback.answer()

@router.callback_query(F.data == "change_language")
async def handle_change_language(callback: CallbackQuery):
    await callback.message.answer("Please select your preferred language 🌐")
    await callback.answer()

# Register the router
dp.include_router(router)

# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
