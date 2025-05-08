import asyncio
from src.bot import start_bot

if __name__ == "__main__":
    # TODO: Make Token getter from environment

    # Bad method
    TOKEN = "7909102868:AAHCCcsrbUIFqGRFYgiiTKQXw1ng3t1oQ7k"
    asyncio.run(start_bot(TOKEN))

