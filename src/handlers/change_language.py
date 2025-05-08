from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command


from src.callbacks.language import LanguageCallback

router = Router()

#TODO: Remake this code, problem with callback_query
@router.callback_query(LanguageCallback)
async def change_language(query: CallbackQuery, callback_data: LanguageCallback):
    print(callback_data.language)
    await query.answer("test1")