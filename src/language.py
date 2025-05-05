import enum
import subprocess
from json import load as json_load
from dataclasses import dataclass

from src.exceptions import NoLanguage, InvalidLanguagePath


@dataclass
class Language(enum.StrEnum):
    RU = 'data/languages/ru.json'
    EN = 'data/languages/en.json'
    LV = 'data/languages/lv.json'

@dataclass
class Context(enum.StrEnum):
    WELCOME = "welcome"



class LanguageManager:
    def __init__(self, language: Language | str = Language.EN) -> None:
        self._language: Language = language
        self._data: dict | None = None

    def set_language(self, language: Language | str = Language.EN) -> None:
        self._language = language

    def has_language(self, language_code: str) -> bool:
        keys = list(Language.__members__.keys())
        return language_code in keys


    # Returns phrase from data/languages/ (if EN -> english phrase, if RU -> russian phrase and etc...)
    def load_data(self) -> dict:
        if self._language:
            if not self._data:
                try:
                    with open(self._language, 'r', encoding='utf-8-sig') as f:
                        return json_load(f)
                except FileNotFoundError:
                    raise InvalidLanguagePath("Check if file of this language exists(data/languages/)\nThere should be a file with name of your language. Current language path: " + self._language)
        else:
            raise NoLanguage("No language is provided to language manager.")

    def get_phrase(self, context: Context) -> str | None:
        if self._data:
            phrase = self._data.get(str(context), None)
            return phrase
        else:
            self._data = self.load_data()
            return self.get_phrase(context)
