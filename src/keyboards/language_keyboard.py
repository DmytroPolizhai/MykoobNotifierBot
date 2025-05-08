from telebot.types import InlineKeyboardButton

from src.keyboards.keyboard import Keyboard
from src.generators.language_generators import generate_language_inline_keyboard_buttons


def change_language_keyboard():
    buttons = generate_language_inline_keyboard_buttons()
    return Keyboard.create_inline_keyboard(buttons, row_width=2)