from aiogram import Bot, Dispatcher

# Routers
from src.handlers.start import router as start_router
from src.handlers.change_language import router as change_language_router

# Run the bot
async def start_bot(token: str) -> None:
    dp = Dispatcher()

    """
    Add routers here to make them work!
    """
    dp.include_routers(start_router, change_language_router)



    bot = Bot(token=token)

    await dp.start_polling(bot)
