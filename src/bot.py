from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode

from language import LanguageManager, Context, LanguageKeyboardManager

import asyncio

from src.stores import UserLanguageStore

TOKEN = "7909102868:AAFfdT5llQ7m8DSo-oFsG6XMXGLBGAqGExY"

dp = Dispatcher()
router = Router()

# Store per-user language preference
user_languages: UserLanguageStore = UserLanguageStore()

@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id
    language_code = message.from_user.language_code.lower() if message.from_user.language_code else "EN"
    lang_manager = LanguageManager(language_code)

    if lang_manager.has_language(language_code):
        user_languages[user_id] = language_code
        phrase = lang_manager.get_phrase(Context.WELCOME)
        await message.answer(phrase, parse_mode=ParseMode.HTML)
    else:
        ...
        # keyboard = InlineKeyboardMarkup(inline_keyboard=[
        #     [
        #         InlineKeyboardButton(text="✅ Yes, English is fine", callback_data="accept_current_language"),
        #         InlineKeyboardButton(text="🌐 No, change language", callback_data="change_language")
        #     ]
        # ])
        # await message.answer(
        #     "Sorry, <b>I don't have your language</b> that you are working with :/\nCould we continue English?",
        #     parse_mode=ParseMode.HTML,
        #     reply_markup=keyboard
        # )
        # user_languages[user_id] = "en"
# TODO: Make universal keyboard manager. Also make language changing
@router.callback_query(F.data == "change_language")
async def handle_change_language(callback: CallbackQuery):
    try:
        keyboard_manager = LanguageKeyboardManager()
        await callback.message.answer("Please select your preferred language 🌐", reply_markup=keyboard_manager.get_language_keyboard())

    except Exception as e:
        print(e)
    finally:
        await callback.answer()



# Run the bot
async def main() -> None:
    dp.include_router(router)
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
