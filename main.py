import os
from aiogram import Bot, Dispatcher, executor, types
from brawl_api import get_club, set_token
from db import add_club

BOT_TOKEN = os.getenv("BOT_TOKEN")
BRAWL_API_TOKEN = os.getenv("BRAWL_API_TOKEN")
ADMINS = list(map(int, os.getenv("ADMINS", "").split(",")))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

set_token(BRAWL_API_TOKEN)

def is_admin(user_id):
    return user_id in ADMINS

@dp.message_handler(commands=["start", "help"])
async def help_cmd(message: types.Message):
    await message.answer(
        "/club TAG — статистика клуба\n"
        "/add_club TAG — добавить клуб"
    )

@dp.message_handler(commands=["add_club"])
async def add_club_cmd(message: types.Message):
    if not is_admin(message.from_user.id):
        return
    tag = message.get_args()
    data = await get_club(tag)
    if "name" not in data:
        await message.answer("❌ Клуб не найден")
        return
    add_club(tag, data["name"])
    await message.answer(f"✅ Клуб {data['name']} добавлен")

@dp.message_handler(commands=["club"])
async def club_cmd(message: types.Message):
    tag = message.get_args()
    data = await get_club(tag)
    if "name" not in data:
        await message.answer("❌ Клуб не найден")
        return
    await message.answer(
        f"🏆 {data['name']}\n"
        f"👥 {len(data['members'])}/30\n"
        f"🏅 Кубки: {data['trophies']}"
    )

if __name__ == "__main__":
    executor.start_polling(dp)
