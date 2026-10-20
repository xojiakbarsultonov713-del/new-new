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
    from aiogram import Bot, Dispatcher, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder

# --- 1. "Maktab Haqida" tugmasi bosilganda ichki menyuni ko'rsatish ---
@dp.callback_query(F.data == "maktab_haqida")  # Sizdagi inline tugmaning callback_data'si
async def about_school_menu(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    
    # Ichki tugmalarni qo'shamiz
    builder.add(types.InlineKeyboardButton(text="ℹ️ Umumiy ma'lumot", callback_data="school_info"))
    builder.add(types.InlineKeyboardButton(text="🏆 Yutuqlarimiz", callback_data="school_achievements"))
    builder.add(types.InlineKeyboardButton(text="📸 Fotogalereya", callback_data="school_gallery"))
    builder.add(types.InlineKeyboardButton(text="⬅️ Bosh menyuga qaytish", callback_data="main_menu"))
    
    # Tugmalarni ustma-ust (1 tadan) joylashtirish
    builder.adjust(1) 
    
    text_msg = (
        "🏫 **18-IDUM (Ixtisoslashtirilgan davlat umumta'lim maktabi) haqida bo'limga xush kelibsiz!**\n\n"
        "Quyidagi tugmalardan birini tanlab, maktabimiz haqida batafsil ma'lumot olishingiz mumkin 👇"
    )
    
    await callback.message.edit_text(
        text=text_msg,
        parse_mode="Markdown",
        reply_markup=builder.as_markup()
    )
    await callback.answer()

# --- 2. "Umumiy ma'lumot" tugmasi uchun handler ---
@dp.callback_query(F.data == "school_info")
async def school_general_info(callback: types.CallbackQuery):
    info_text = (
        "ℹ️ **Maktab haqida umumiy ma'lumotlar:**\n\n"
        "📍 **Manzil:** [Maktab joylashgan ko'cha va tuman nomi]\n"
        "📞 **Telefon:** +998 (XX) XXX-XX-XX\n"
        "👤 **Maktab direktori:** [Ism-sharifi]\n"
        "⏰ **Ish tartibi:** 08:00 - 17:00\n\n"
        "Maktabimiz zamonaviy AKT xonalari, sun'iy intellekt laboratoriyasi va barcha qulayliklarga ega!"
    )
    
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="⬅️ Orqaga", callback_data="maktab_haqida"))
    
    await callback.message.edit_text(text=info_text, parse_mode="Markdown", reply_markup=builder.as_markup())
    await callback.answer()

# --- 3. "Yutuqlarimiz" tugmasi uchun handler ---
@dp.callback_query(F.data == "school_achievements")
async def school_achievements_info(callback: types.CallbackQuery):
    achievements_text = (
        "🏆 **Maktabimiz yutuqlari:**\n\n"
        "🥇 Fan olimpiadalarida tuman va viloyat bosqichida faxrli o'rinlar.\n"
        "🤖 IT va Sun'iy intellekt yo'nalishidagi tanlovlar g'oliblari.\n"
        "⚽️ Sport musobaqalarida maktab jamoasining muvaffaqiyatlari.\n\n"
        "Biz o'quvchilarimiz bilan faxrlanamiz! 🎉"
    )
    
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="⬅️ Orqaga", callback_data="maktab_haqida"))
    
    await callback.message.edit_text(text=achievements_text, parse_mode="Markdown", reply_markup=builder.as_markup())
    await callback.answer()
