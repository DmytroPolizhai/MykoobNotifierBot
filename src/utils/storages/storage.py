from json import dump, load, JSONDecodeError
from src.utils.misc.singleton import Singleton


class Storage(dict, metaclass=Singleton):
    def __init__(self, save_path: str, **kwargs) -> None:
        super().__init__()
        self._old_storage: dict = {}
        self._containers: dict = kwargs
        self._save_path: str = save_path  # Ensure _save_path is set
        self.load()

    def __setitem__(self, key, value):
        str_key = str(key)
        str_value = str(value)

        self._containers[str_key] = str_value
        super().__setattr__(str_key, str_value)
        self.save()

    def load(self):
        """Loads JSON data from the file, initializing an empty JSON object on errors."""
        try:
            with open(self._save_path, "r", encoding='utf-8-sig') as f:
                self._old_storage = load(f)
        except (FileNotFoundError, JSONDecodeError):
            # If the file does not exist or contains invalid JSON, initialize as empty
            self._old_storage = {}
            self._containers = {}
            self.save()

    def save(self):
        """Writes JSON data from the containers to the file."""
        with open(self._save_path, "w", encoding='utf-8-sig') as f:
            dump(self._containers, f, ensure_ascii=False, indent=4)
