from aiogram import Bot, Dispatcher, F, Router

# Routers
from src.handlers.start import router as start_router

# Run the bot
async def start_bot(token: str) -> None:
    dp = Dispatcher()

    """
    Add routers here to make them work!
    """
    dp.include_routers(start_router)



    bot = Bot(token=token)

    await dp.start_polling(bot)
