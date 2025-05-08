from aiogram.filters.callback_data import CallbackData

class LanguageCallback(CallbackData, prefix="language"):
    language: str