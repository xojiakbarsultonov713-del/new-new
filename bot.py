import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from google import genai
from google.genai import types as gemini_types

# --- TOKEN VA SOZLAMALAR ---
BOT_TOKEN = "8620955124:AAHXLEXPjTyNT5t_FADWc4k_0kXbtWKkVVA"
# Sizning API kalitingiz bu yerga aniq joylashtirildi:
GEMINI_API_KEY = "AQAb8RN6KyZE4v-Azo6IipsM_e3L6XwTuwvj_0IBNtstDC_cF8GA" 

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Gemini AI klientini ishga tushiramiz
ai_client = genai.Client(api_key=GEMINI_API_KEY)

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
        f"Menyulardan foydalanishingiz yoki menga maktab va IT bo'yicha to'g'ridan-to'g'ri savol yozishingiz mumkin. Men sizga yordam beruvchi aqlli AI yordamchiman! 🤖\n\n"
        f"Quyidagi menyulardan kerakli bo'limni tanlang:",
        reply_markup=main_menu(),
        parse_mode="Markdown"
    )

# --- TUGMA BOSILGANDA ISHLAYDIGAN FUNKSIYALAR ---

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

@dp.callback_query(F.data == "rating")
async def cb_rating(callback: types.CallbackQuery):
    await callback.message.answer("📊 Koordinatorlar Reytingi 🏆:\n\nFaol ishtirokchilar va koordinatorlarning onlayn reyting diagrammasi.", parse_mode="Markdown")
    await callback.answer()

# --- MAKTAB HAQIDA ICHKI MENYUSI ---

@dp.callback_query(F.data == "about")
async def about_school_menu(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="ℹ️ Umumiy ma'lumot", callback_data="school_info"))
    builder.add(types.InlineKeyboardButton(text="🏆 Yutuqlarimiz", callback_data="school_achievements"))
    builder.add(types.InlineKeyboardButton(text="📸 Fotogalereya", callback_data="school_gallery"))
    builder.add(types.InlineKeyboardButton(text="⬅️ Bosh menyuga qaytish", callback_data="main_menu"))
    builder.adjust(1) 
    
    text_msg = (
        "🏫 **18-IDUM (Ixtisoslashtirilgan davlat umumta'lim maktabi) haqida bo'limga xush kelibsiz!**\n\n"
        "Quyidagi tugmalardan birini tanlab, maktabimiz haqida batafsil ma'lumot olishingiz mumkin 👇"
    )
    await callback.message.edit_text(text=text_msg, parse_mode="Markdown", reply_markup=builder.as_markup())
    await callback.answer()

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
    builder.add(types.InlineKeyboardButton(text="⬅️ Orqaga", callback_data="about"))
    await callback.message.edit_text(text=info_text, parse_mode="Markdown", reply_markup=builder.as_markup())
    await callback.answer()

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
    builder.add(types.InlineKeyboardButton(text="⬅️ Orqaga", callback_data="about"))
    await callback.message.edit_text(text=achievements_text, parse_mode="Markdown", reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "school_gallery")
async def school_gallery_info(callback: types.CallbackQuery):
    gallery_text = "📸 **Maktab fotogalereyasi:**\n\nTez kunda bu yerga maktab hayotidan foto va videolar qo'shiladi."
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="⬅️ Orqaga", callback_data="about"))
    await callback.message.edit_text(text=gallery_text, parse_mode="Markdown", reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "main_menu")
async def back_to_main_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text="Quyidagi menyulardan kerakli bo'limni tanlang:",
        reply_markup=main_menu()
    )
    await callback.answer()

# --- SUN'IY INTELLEKT (AI) YORDAMCHI FUNKSIYASI ---
@dp.message()
async def ai_assistant_handler(message: types.Message):
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    
    try:
        response = ai_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=message.text,
            config=gemini_types.GenerateContentConfig(
                system_instruction=(
                    "Siz 18-sonli ixtisoslashtirilgan davlat umumta'lim maktabining (IDUM) rasmiy botidagi aqlli AI yordamchisiz. "
                    "Foydalanuvchilarga juda muloyim, hurmat bilan va aniq javob bering. "
                    "Maktab hayoti, o'qish, matematika, fizika hamda IT & AI to'garaklari haqidagi savollarga qunt bilan javob bering. "
                    "Doimo chiroyli o'zbek tilida javob qaytaring va kerakli joyda emojilardan foydalaning."
                )
            )
        )
        await message.answer(response.text)
    except Exception as e:
        await message.answer("⚠️ Tizimda kichik texnik uzilish yuz berdi. Iltimos, birozdan so'ng qayta urinib ko'ring.")

async def main():
    print("🤖 Bot muvaffaqiyatli ishga tushdi va AI faollashtirildi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
GEMINI_API_KEY = "AQ.Ab8RN6JIccvWUljRJVJKZn7Ch14wx9D60ixO0HE7c5y6KJahqQ"
