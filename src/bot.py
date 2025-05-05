import telebot


class TelegramBot:
    def __init__(self, token: str) -> None:
        self._token = token
        self._api = telebot.TeleBot(token)



if __name__ == "__main__":
    from dotenv import load_dotenv
    from os import getenv

    load_dotenv()
    TOKEN = getenv("TOKEN")

    bot = TelegramBot(TOKEN)