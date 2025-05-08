@router.callback_query(F.data == "change_language")
async def handle_change_language(callback: CallbackQuery):
    try:
        keyboard_manager = LanguageKeyboardManager()
        await callback.message.answer("Please select your preferred language 🌐", reply_markup=keyboard_manager.get_language_keyboard())

    except Exception as e:
        print(e)
    finally:
        await callback.answer()