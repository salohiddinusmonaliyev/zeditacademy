from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

milliy = KeyboardButton("🇺🇿 Milliy Taomlar")
fast = KeyboardButton("🌭 Fast Food")
water = KeyboardButton("🍾 Ichimliklar")
foodsKey = ReplyKeyboardMarkup(resize_keyboard=True).add(milliy, water).add(fast)