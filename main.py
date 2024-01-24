import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import CommandStart, Command
from config import TOKEN
from messages import MSG_START, MSG_ASSISTANT, MSG_REMIND, MSG_INPUT_FIELD, CMD_CHAT, CMD_REMIND
import g4f

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command(CMD_CHAT))
@dp.message(F.text.lower() == MSG_ASSISTANT.lower())
async def chat_gpt(message: types.Message):
    await message.answer("Подожди, дай мне подумать...")
    response = await g4f.ChatCompletion.create_async(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": message.text}],
        provider=g4f.Provider.GeekGpt
    )
    await bot.edit_message_text(
        response,
        message.chat.id,
        message.message_id + 1
    )


@dp.message(CommandStart())
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


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
