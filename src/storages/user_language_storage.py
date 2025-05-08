from src.config import USERS_LANG_PATH
from src.storages.storage import Storage

class UserLanguageStorage(Storage):
    def __init__(self, **kwargs) -> None:
        super().__init__(USERS_LANG_PATH, **kwargs)