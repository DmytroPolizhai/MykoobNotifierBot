import os
import json
from collections import defaultdict

from src.config import LANGUAGES_PATH


def get_language_codes() -> dict[str, str]:
    language_names = defaultdict()

    for file_name in os.listdir(LANGUAGES_PATH):
        if file_name.endswith(".json"):
            name = file_name.removesuffix(".json")
            path = os.path.join(LANGUAGES_PATH, file_name)

            language_names[name] = path

    return language_names
