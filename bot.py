import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Tokeningiz o'rnatildi:
BOT_TOKEN = "8620955124:AAHXLEXPjTyNT5t_FADWc4k_0kXbtWKkVVA"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# --- ASOSIY MENYU TUGMALARI ---
def main_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📰 Maktab Yangiliklari", callback_data="news"),
            InlineKeyboardButton(text="📅 Dars Jadvali", callback_data="schedule")
        ],
        [
            InlineKeyboardButton(text="📚 O'quv Materiallari", callback_data="materials"),
            InlineKeyboardButton(text="🤖 IT & AI Klubi", callback_data="it_club")
        ],
        [
            InlineKeyboardButton(text="👥 Koordinatorlar", callback_data="coordinators"),
            InlineKeyboardButton(text="📝 Murojaat Qoldirish", callback_data="contact")
        ],
        [
            InlineKeyboardButton(text="ℹ️ Maktab Haqida", callback_data="about")
        ],
        [
            InlineKeyboardButton(text="📊 Koordinatorlar Reytingi 🏆", callback_data="rating")
        ]
    ])
    return keyboard

# /start buyrug'i
@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        f"Salom, {message.from_user.first_name}! 👋\n\n"
        f"18-Maktabning rasmiy Smart Botiga xush kelibsiz!\n"
        f"Quyidagi menyulardan kerakli bo'limni tanlang:",
        reply_markup=main_menu(),
        parse_mode="Markdown"
    )

# --- 8 TA TUGMA BOSILGANDA ISHLaydigan FUNKSIYALAR ---

@dp.callback_query(F.data == "news")
async def cb_news(callback: types.CallbackQuery):
    await callback.message.answer("📰 Maktab yangiliklari:\n\nTez kunda shu yerda 18-maktabning eng so'nggi yangiliklari va Telegra.ph havolalari joylab boriladi.", parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "schedule")
async def cb_schedule(callback: types.CallbackQuery):
    await callback.message.answer("📅 Dars jadvali:\n\nBu bo'limda sinflar kesimidagi dars jadvallari ko'rsatiladi.", parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "materials")
async def cb_materials(callback: types.CallbackQuery):
    await callback.message.answer("📚 O'quv materiallari:\n\nO'qituvchilar va o'quvchilar uchun foydali darsliklar hamda qo'llanmalar (Telegra.ph orqali).", parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "it_club")
async def cb_it_club(callback: types.CallbackQuery):
    await callback.message.answer("🤖 IT & AI Klubi:\n\n18-maktabning IT va sun'iy intellekt to'garaklari, dars kunlari va qilinayotgan loyihalar.", parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "coordinators")
async def cb_coordinators(callback: types.CallbackQuery):
    await callback.message.answer("👥 IT/AI Koordinatorlar:\n\nMaktabimizdagi mas'ul IT va AI koordinatorlari haqida ma'lumot.", parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "contact")
async def cb_contact(callback: types.CallbackQuery):
    await callback.message.answer("📝 Murojaat qoldirish:\n\nTaklif, shikoyat yoki savollaringiz bo'lsa yuborishingiz mumkin. Tez orada adminlarga yo'naltiriladi.", parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "about")
async def cb_about(callback: types.CallbackQuery):
    await callback.message.answer("ℹ️ 18-Maktab haqida:\n\nMaktabimiz tarixi, erishgan yutuqlari va asosiy ma'lumotlar.", parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "rating")
async def cb_rating(callback: types.CallbackQuery):
    await callback.message.answer("📊 Koordinatorlar Reytingi 🏆:\n\nFaol ishtirokchilar va koordinatorlarning onlayn reyting diagrammasi.", parse_mode="Markdown")
    await callback.answer()
# Istalgan matnli xabarga javob berish uchun handler
@dp.message()
async def echo_message(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")
async def main():
    print("🤖 Bot muvaffaqiyatli ishga tushdi va xabarlarni kutmoqda...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())