from aiogram.types import InlineKeyboardButton

from src.utils.folder_scanner import get_language_codes
from src.callbacks.language import LanguageCallback


def generate_language_inline_keyboard_buttons() -> list[list[InlineKeyboardButton]]:
    """
    Generate language inline keyboard buttons from available language codes in "database"
    :return:
    """

    available_codes: dict = get_language_codes()
    output: list[list[InlineKeyboardButton]] = [[]]

    for code in available_codes:
        callback = LanguageCallback(language=code)
        button = InlineKeyboardButton(text=code, callback_data=callback.pack())
        output[0].append(button)

    return output
