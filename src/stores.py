from json import load as json_load
from json import dump as json_dump
from src.config import USERS_LANG_PATH
class Store(dict):
    def __init__(self, save_path: str, **kwargs) -> None:
        super().__init__()
        self._containers: dict = kwargs
        self._save_path: str = save_path  # Ensure _save_path is set
        self.save_store()

    def __setitem__(self, key, value):
        str_key = str(key)
        str_value = str(value)

        self._containers[str_key] = str_value
        super().__setattr__(str_key, str_value)
        self.save_store()

    def save_store(self):
        with open(self._save_path, "w", encoding='utf-8-sig') as f:
            json_dump(self._containers, f, ensure_ascii=False, indent=4)


class UserLanguageStore(Store):
    def __init__(self, **kwargs) -> None:
        super().__init__(USERS_LANG_PATH, **kwargs)