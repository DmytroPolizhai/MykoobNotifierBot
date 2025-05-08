from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command

from src.storages.user_language_storage import UserLanguageStorage
from src.managers.language_manager import LanguageManager
from src.keyboards.language_keyboard import change_language_keyboard

router = Router()
user_language_storage: UserLanguageStorage = UserLanguageStorage()

@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id

    if user_id in user_language_storage:
        language = user_language_storage[user_id]
    else:
        language = message.from_user.language_code.lower() if message.from_user.language_code else "en"
        user_language_storage[user_id] = language

    language_manager = LanguageManager()

    if language_manager.has_language(language):
        language_manager.set_language(language)

    phrase = language_manager.get_phrase("greeting")

    await message.answer(phrase, parse_mode=ParseMode.HTML, reply_markup=change_language_keyboard())
