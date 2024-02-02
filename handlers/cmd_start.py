from aiogram import Router, types
from aiogram.filters.command import CommandStart, Command
from messages import MSG_START, MSG_ASSISTANT, MSG_REMIND, MSG_INPUT_FIELD

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    print(message.chat.id)
    kb = [
        [types.KeyboardButton(text=MSG_ASSISTANT)],
        [types.KeyboardButton(text=MSG_REMIND)]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=MSG_INPUT_FIELD
    )
    await message.answer(MSG_START.format(message.chat.full_name), reply_markup=keyboard)
