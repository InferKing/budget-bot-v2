from aiogram import F, types, Router
from aiogram.filters.command import Command
from messages import CMD_CHAT, MSG_ASSISTANT
import g4f

router = Router()


@router.message(Command(CMD_CHAT))
@router.message(F.text.lower() == MSG_ASSISTANT.lower())
async def chat_gpt(message: types.Message):
    await message.answer(
        g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=[{"role": "user", "content": message.text}],
            provider=g4f.Provider.GeekGpt
        )
    )
    # await bot.edit_message_text(
    #     response,
    #     message.chat.id,
    #     message.message_id + 1
    # )
