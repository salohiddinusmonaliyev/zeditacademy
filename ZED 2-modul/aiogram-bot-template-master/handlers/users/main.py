import logging

from aiogram import Bot, Dispatcher, executor, types

from data.config import ADMINS
from loader import dp

from aiogram.types import CallbackQuery

from keyboards.default.startKey import foodsKey
from keyboards.inline.meals import milliyKey, waterKey, fastKey, menu

@dp.message_handler(text="🔙 Ortga")
async def back(message: types.Message):
    await message.reply("🔙 Ortga", reply_markup=foodsKey)

@dp.message_handler(text="🔛 Bosh menyu")
async def back(message: types.Message):
    await message.reply("🔛 Bosh menyu", reply_markup=foodsKey)

@dp.message_handler(text="🇺🇿 Milliy Taomlar")
async def milliy(message: types.Message):
    await message.reply("Milliy taomlardan birini tanlang: ", reply_markup=milliyKey)

@dp.message_handler(text="🌭 Fast Food")
async def fastfood(message: types.Message):
    await message.reply("Fast Food taomlardan birini tanlang: ", reply_markup=fastKey)

@dp.message_handler(text="🍾 Ichimliklar")
async def water(message: types.Message):
    await message.reply("Ichimliklardan birini tanlang: ", reply_markup=waterKey)

@dp.message_handler(content_types="locatsion")
async def locat(message: types.Message):
    await message.reply("Joylashuv qabul qilindi. Tez orada buyurtmangiz yetqazib beriladi.", reply_markup=foodsKey)

@dp.callback_query_handler(text=["pepsi", "cola", "palov"])
async def echos(call: CallbackQuery):
    await call.message.answer_photo(photo=open(f"handlers/users/images/{call.data}.jpg", 'rb'), caption=f"Siz {call.data}ni buyurtma bermoqchisiz.", reply_markup=menu)

    @dp.message_handler(content_types="contact", is_sender_contact=False)
    async def contact(message: types.Message):
        await message.reply("Kontakt qubul qilindi. Siz bilan tez orada operatr bog'lanadi.", reply_markup=foodsKey)

    @dp.message_handler(content_types="contact", is_sender_contact=True)
    async def contact(message: types.Message):
        await message.reply("Kontakt qubul qilindi. Siz bilan tez orada operatr bog'lanadi.", reply_markup=foodsKey)

        try:
            await dp.bot.send_message(639677412, f"Buyurtma bor:\n\n<b>Telefon raqami:</b> {message.contact.phone_number}\n<b>Buyurtma berdi:</b> {call.data}")

        except Exception as err:
            logging.exception(err)
    await call.answer(cache_time=5)
