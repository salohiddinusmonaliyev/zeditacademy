"""
 This is a echo bot.
 It echoes any incoming text messages.
 """

import logging

from aiogram import Bot, Dispatcher, executor, types

import requests

API_TOKEN = '5472551030:AAFG7VFa7N7MBiVgHVSRYPy9sJL5FDGp7r0'

# Configure logging
logging.basicConfig(level=logging.INFO)

r = requests.request(method="GET", url="https://islomapi.uz/api/present/day?region=Toshkent")

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom")

@dp.message_handler(commands=['fergana'])
async def fergana(message: types.Message):
    url = f"https://islomapi.uz/api/present/day?region=Farg%27оna"
    r = requests.get(url)
    date = r.json()['date']
    week = r.json()['weekday']
    time = r.json()['times']
    saharlik = time['tong_saharlik']
    quyosh = time['quyosh']
    peshin = time['peshin']
    asr = time['asr']
    shom = time['shom_iftor']
    hufton = time['hufton']
    region = r.json()['region']
    await message.reply(f"Namoz vaqtlari 2️⃣0️⃣2️⃣2️⃣\n\n{region}\n\nSana: {date}\nKun: {week}\n\nBomdod: {saharlik}\nQuyosh: {quyosh}\nPeshin: {peshin}\nAsr: {asr}\nShom: {shom}\nXufton: {hufton}")

@dp.message_handler(commands=['programmer'])
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer("Usmonaliyev Salohidddin")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)