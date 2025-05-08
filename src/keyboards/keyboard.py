from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class Keyboard:
    """
    A general class for creating keyboards using aiogram's InlineKeyboardMarkup and InlineKeyboardButton.
    """

    @staticmethod
    def create_inline_keyboard(buttons: list[list[InlineKeyboardButton]], row_width: int = 1) -> InlineKeyboardMarkup:
        """
        Creates an InlineKeyboardMarkup with the specified buttons.

        Args:
            buttons (list[list[InlineKeyboardButton]]): A nested list where each element is an InlineKeyboardButton.
                                                        Example: [[InlineKeyboardButton(text="Button1", callback_data="data1")],
                                                                  [InlineKeyboardButton(text="Button2", callback_data="data2")]].
            row_width (int): The maximum number of buttons per row.

        Returns:
            InlineKeyboardMarkup: Generated inline keyboard markup object.
        """
        inline_keyboard = [[*row] for row in buttons]

        return InlineKeyboardMarkup(inline_keyboard=inline_keyboard, row_width=row_width)
