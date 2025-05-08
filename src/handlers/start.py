from typing import Optional

from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command

from src.utils.storages.user_language_storage import UserLanguageStorage
from src.utils.managers.language_manager import LanguageManager

router = Router()
user_language_storage: UserLanguageStorage = UserLanguageStorage()

@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id
    language: Optional[str] = None

    if user_id in user_language_storage:
        language = user_language_storage[user_id]
    else:
        language = message.from_user.language_code.lower() if message.from_user.language_code else "en"

    language_manager = LanguageManager()

    if language_manager.has_language(language):
        language_manager.set_language(language)

    phrase = language_manager.get_phrase("greeting")

    await message.answer(phrase, parse_mode=ParseMode.HTML)