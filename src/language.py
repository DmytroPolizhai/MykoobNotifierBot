import json
import enum
from typing import Optional
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.exceptions import NoLanguage, InvalidLanguagePath
from src.config import LANG_SETUP_PATH

LANGUAGE_CODES = json.load(open(LANG_SETUP_PATH, 'r', encoding="utf-8-sig"))

class Context(enum.StrEnum):
    WELCOME = "welcome"

class LanguageManager:
    def __init__(self, language_code: str = "en") -> None:
        self._language_code: str = language_code.lower()
        self._data: Optional[dict] = None

    def set_language(self, language_code: str) -> None:
        if not self.has_language(language_code):
            raise NoLanguage(f"Language '{language_code}' not supported.")
        self._language_code = language_code.upper()
        self._data = None

    @staticmethod
    def has_language(language_code: str) -> bool:
        return language_code.lower() in LANGUAGE_CODES

    def load_data(self) -> dict:
        if not self._language_code:
            raise NoLanguage("No language is provided to language manager.")

        if not self._data:
            path = LANGUAGE_CODES.get(self._language_code)
            try:
                with open(path, 'r', encoding='utf-8-sig') as f:
                    self._data = json.load(f)
            except FileNotFoundError:
                raise InvalidLanguagePath(f"Language file not found at: {path}")
        return self._data

    def get_phrase(self, context: Context) -> Optional[str]:
        if not self._data:
            self.load_data()
        return self._data.get(str(context))

        # keyboard = InlineKeyboardMarkup(inline_keyboard=[
        #     [
        #         InlineKeyboardButton(text="✅ Yes, English is fine", callback_data="accept_current_language"),
        #         InlineKeyboardButton(text="🌐 No, change language", callback_data="change_language")
        #     ]
        # ])
class LanguageKeyboardManager:
    @staticmethod
    def get_language_keyboard() -> InlineKeyboardMarkup:
        buttons: list[InlineKeyboardButton] = []

        for code, _ in LANGUAGE_CODES.items():
            button = InlineKeyboardButton(text=code, callback_data=f"change_language:{code}")
            buttons.append(button)
        return InlineKeyboardMarkup(inline_keyboard=[buttons])
