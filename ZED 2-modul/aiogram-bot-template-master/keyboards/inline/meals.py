from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

palov = InlineKeyboardButton("Osh", callback_data="palov")
lagmon = InlineKeyboardButton("Lag'mon", callback_data="lagman")
milliyKey = InlineKeyboardMarkup().add(palov, lagmon)

cola = InlineKeyboardButton("Coka Cola", callback_data="cola")
pepsi = InlineKeyboardButton("Pepsi", callback_data="pepsi")
waterKey = InlineKeyboardMarkup().add(cola, pepsi)

hotdog = InlineKeyboardButton("Hot Dog", callback_data="hotdog")
hamburger = InlineKeyboardButton("Hamburger", callback_data="hamburger")
fastKey = InlineKeyboardMarkup().add(hotdog, hamburger)

main = KeyboardButton("🔛 Bosh menyu")
contact = KeyboardButton("📞 Kontaktni ulashish", request_contact=True)
location = KeyboardButton("📍 Joylashuvni ulashish", request_location=True)
back = KeyboardButton("🔙 Ortga")
Key = ReplyKeyboardMarkup(resize_keyboard=True).add(contact).add(main, back)
menu = ReplyKeyboardMarkup(resize_keyboard=True).add(contact, location)