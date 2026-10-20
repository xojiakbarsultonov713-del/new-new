import asyncio
import requests
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# --- TOKEN VA SOZLAMALAR ---
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
        f"Menyulardan foydalanishingiz yoki menga to'g'ridan-to'g'ri savol yozishingiz mumkin. Men sizga yordam beruvchi AI yordamchiman! 🤖",
        reply_markup=main_menu(),
        parse_mode="Markdown"
    )

# --- TUGMA BOSILGANDA ISHLAYDIGAN FUNKSIYALAR ---
@dp.callback_query(F.data == "news")
async def cb_news(callback: types.CallbackQuery):
    await callback.message.answer("📰 Maktab yangiliklari:\n\nTez kunda shu yerda 18-maktabning eng so'nggi yangiliklari joylab boriladi.")
    await callback.answer()

@dp.callback_query(F.data == "schedule")
async def cb_schedule(callback: types.CallbackQuery):
    await callback.message.answer("📅 Dars jadvali:\n\nBu bo'limda sinflar kesimidagi dars jadvallari ko'rsatiladi.")
    await callback.answer()

@dp.callback_query(F.data == "materials")
async def cb_materials(callback: types.CallbackQuery):
    await callback.message.answer("📚 O'quv materiallari:\n\nO'qituvchilar va o'quvchilar uchun foydali darsliklar hamda qo'llanmalar.")
    await callback.answer()

@dp.callback_query(F.data == "it_club")
async def cb_it_club(callback: types.CallbackQuery):
    await callback.message.answer("🤖 IT & AI Klubi:\n\n18-maktabning IT va sun'iy intellekt to'garaklari haqida ma'lumot.")
    await callback.answer()

@dp.callback_query(F.data == "coordinators")
async def cb_coordinators(callback: types.CallbackQuery):
    await callback.message.answer("👥 IT/AI Koordinatorlar:\n\nMaktabimizdagi mas'ul IT va AI koordinatorlari haqida ma'lumot.")
    await callback.answer()

@dp.callback_query(F.data == "contact")
async def cb_contact(callback: types.CallbackQuery):
    await callback.message.answer("📝 Murojaat qoldirish:\n\nTaklif, shikoyat yoki savollaringiz bo'lsa yuborishingiz mumkin.")
    await callback.answer()

@dp.callback_query(F.data == "rating")
async def cb_rating(callback: types.CallbackQuery):
    await callback.message.answer("📊 Koordinatorlar Reytingi 🏆:\n\nFaol ishtirokchilar va koordinatorlarning onlayn reyting diagrammasi.")
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
    
    await callback.message.edit_text(
        text="🏫 **18-IDUM haqida bo'limga xush kelibsiz!**\n\nQuyidagi tugmalardan birini tanlang:",
        parse_mode="Markdown",
        reply_markup=builder.as_markup()
    )
    await callback.answer()

@dp.callback_query(F.data == "school_info")
async def school_general_info(callback: types.CallbackQuery):
    info_text = "ℹ️ **Maktab haqida umumiy ma'lumotlar:**\n\n📍 **Manzil:** Maktab ko'chasi\n📞 **Telefon:** +998 (XX) XXX-XX-XX"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="⬅️ Orqaga", callback_data="about"))
    await callback.message.edit_text(text=info_text, parse_mode="Markdown", reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "school_achievements")
async def school_achievements_info(callback: types.CallbackQuery):
    achievements_text = "🏆 **Maktabimiz yutuqlari:**\n\n🥇 Fan olimpiadalari va IT tanlovlar g'oliblari."
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="⬅️ Orqaga", callback_data="about"))
    await callback.message.edit_text(text=achievements_text, parse_mode="Markdown", reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "school_gallery")
async def school_gallery_info(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="⬅️ Orqaga", callback_data="about"))
    await callback.message.edit_text(text="📸 Tez kunda foto va videolar qo'shiladi.", reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "main_menu")
async def back_to_main_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(text="Quyidagi menyulardan kerakli bo'limni tanlang:", reply_markup=main_menu())
    await callback.answer()

# --- SUN'IY INTELLEKT (MUTLAQO BEPUL VA KALITSIZ) ---
@dp.message()
async def ai_assistant_handler(message: types.Message):
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    
    # Yuklanish xabarini chiqarib turamiz
    waiting_msg = await message.answer("🤖 *Sun'iy intellekt o'ylamoqda...*", parse_mode="Markdown")
    
    # Ochiq va bepul sun'iy intellekt API'si
    url = f"https://browsergpts.com"
    
    payload = {
        "messages": [
            {"role": "system", "content": "Siz 18-sonli maktabning rasmiy AI yordamchisiz. O'zbek tilida chiroyli javob bering."},
            {"role": "user", "content": message.text}
        ]
    }
    
    try:
        response = requests.post(url, json=payload, timeout=15)
        # Kelgan matnli javobni tozalaymiz
        ai_response = response.text.strip()
        
        if ai_response:
            await waiting_msg.edit_text(ai_response)
        else:
            await waiting_msg.edit_text("🤖 Hozircha javob topolmadim, birozdan so'ng qayta so'rab ko'ring.")
    except Exception as e:
        await waiting_msg.edit_text("🤖 Hozircha AI band, iltimos menyu tugmalaridan foydalanib turing!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

