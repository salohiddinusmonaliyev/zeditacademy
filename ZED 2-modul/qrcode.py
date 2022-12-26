"""
This is a echo bot.
It echoes any incoming text messages
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

import pyqrcode

API_TOKEN = '5472551030:AAFG7VFa7N7MBiVgHVSRYPy9sJL5FDGp7r0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)0
    q = pyqrcode.create(f"https://www.youtube.com/results?search_query={message.text}")
    q.png('qr.png', scale=20)
    await message.answer_photo(photo=open("qr.png", 'rb'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)