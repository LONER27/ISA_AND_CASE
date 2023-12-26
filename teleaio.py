import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery
import requests

appid = 'ad1a1a42eab275e6bb7e9532cfcd52c2'

res = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=55.191&lon=30.203",
                   params={'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

logging.basicConfig(level=logging.INFO)

bot = Bot(token='1120486477:AAFJhpujfVdsEftw8HHo8CvGgrITUtpsXYA')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    choose1 = types.InlineKeyboardButton(text='Погода', callback_data='pogoda')
    markup.add(choose1)
    await message.reply("Привет\nЭто пока проба", reply_markup=markup)


@dp.callback_query_handler(text='pogoda')
async def send_message(call: CallbackQuery):
    await call.message.answer(f"Осадки: {data['list'][0]['weather'][0]['description']}\n"
                              f"Температура сейчас: {data['list'][0]['main']['temp']}\u00b0C\n"
                              f"Ощущается как: {data['list'][0]['main']['feels_like']}\u00b0C\n"
                              f"Мин. возможная температура: {data['list'][0]['main']['temp_min']}\u00b0C\n"
                              f"Макс. возможная температура: {data['list'][0]['main']['temp_max']}\u00b0C\n"
                              f"Видимость: {data['list'][0]['main']['humidity']}%\n"
                              f"Давление: {data['list'][0]['main']['pressure']}hPa\n"
                              f"Скорость ветра: {data['list'][0]['wind']['speed']}м/с",
                              parse_mode='html')


@dp.message_handler(content_types=['text'])
async def talk(message: types.Message):
    markip = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    weer = types.KeyboardButton('Погода в Витебске')
    markip.add(weer)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
