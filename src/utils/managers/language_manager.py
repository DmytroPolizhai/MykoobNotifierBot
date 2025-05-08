import json
from typing import Optional

from src.utils.misc.enums import Context
from src.utils.misc.folder_scanner import get_language_codes
from src.utils.managers.manager import Manager


class LanguageManager(Manager):
    def __init__(self, start_code: str = "en", **kwargs) -> None:
        """
        Initialize the LanguageManager with a starting language code.
        """
        super().__init__(**kwargs)
        self._current_code: Optional[str] = None
        self._data: Optional[dict] = None
        self._language_codes = self._initialize_language_codes()

        self.set_language(start_code)

    def _initialize_language_codes(self) -> dict:
        """
        Initialize codes for supported languages by calling an external function.
        Returns a dictionary of language codes and their associated file paths.
        """
        # Error handling in case `get_language_codes` fails
        try:
            codes = get_language_codes()
        except Exception as e:
            raise RuntimeError(f"Failed to initialize language codes: {e}")

        if not codes:
            raise ValueError("No language codes provided.")

        return codes

    def set_language(self, new_language_code: str) -> None:
        """
        Set the current language code and load its data.
        Raises an exception if the language code is invalid or unsupported.
        """
        if self.has_language(new_language_code):
            self._current_code = new_language_code.lower()
            self._data = self._load_language_data()
        else:
            raise ValueError(f"Invalid or unsupported language code: {new_language_code}")

    def has_language(self, language_code: str) -> bool:
        """
        Check if the given language code is available.
        """
        return language_code.lower() in self._language_codes

    def get_phrase(self, context: Context | str) -> Optional[str]:
        """
        Retrieve the phrase associated with the given context.
        Returns None if the data is not loaded or the context is not found.
        """
        if not self._data:
            return None

        return self._data.get(str(context), None)

    def _load_language_data(self) -> dict:
        """
        Load language data from the file corresponding to the current language code.
        Returns an empty dictionary if loading fails.
        """
        if not self._current_code or self._current_code not in self._language_codes:
            raise ValueError(f"No data available for language: {self._current_code}")

        path = self._language_codes[self._current_code]

        try:
            with open(path, 'r', encoding='utf-8-sig') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Language file not found: {path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in language file {path}: {e}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error while loading language data: {e}")


if __name__ == "__main__":
    try:
        # Initialize language manager with 'en' and demonstrate functionality
        language_manager = LanguageManager("en")
        print(language_manager.get_phrase(Context.WELCOME))

        language_manager.set_language("lv")
        print(language_manager.get_phrase(Context.WELCOME))

    except Exception as e:
        print(f"Error: {e}")
