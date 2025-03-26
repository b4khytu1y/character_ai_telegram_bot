import logging
import asyncio
import httpx
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = '8025483084:AAH_CgKKebA0UUi_mKEKzk82YenNSQ2Li4M'  # замени на свой токен от BotFather
CHARACTER_TOKEN = 'ab0fb6d0ce6889984782c8e3eb33667fad9fc361'
CHARACTER_ID = 'zQ7Yav1HdV_MzCUsXRaKbeVZuEoLOvlpXn2pSKr-LEU'  # нужно указать конкретный ID персонажа


bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

async def get_character_reply(user_msg: str):
    headers = {
        'Authorization': f'Token {CHARACTER_TOKEN}'
    }
    async with httpx.AsyncClient() as client:
        payload = {
            "character_external_id": CHARACTER_ID,
            "text": user_msg,
            "tgt": CHARACTER_ID,
        }
        response = await client.post(
            "https://beta.character.ai/chat/streaming/",
            json=payload,
            headers=headers,
            timeout=30.0
        )

        if response.status_code == 200:
            try:
                for line in response.iter_lines():
                    if line and b'replies' in line:
                        return "Ответ от персонажа"  # здесь можно парсить json из line
            except Exception as e:
                return f"Ошибка парсинга: {e}"
        else:
            return f"Ошибка CharacterAI: {response.status_code}"

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Я бот-собеседник. Напиши мне что-нибудь!")

@dp.message()
async def handle_message(message: Message):
    await message.answer("⌛ Думаю...")
    reply = await get_character_reply(message.text)
    await message.answer(reply or "Что-то пошло не так.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())