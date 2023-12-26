import telebot
from telebot import types
import requests

appid = 'ad1a1a42eab275e6bb7e9532cfcd52c2'

res = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=55.191&lon=30.203", params={'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

bot = telebot.TeleBot('1120486477:AAFJhpujfVdsEftw8HHo8CvGgrITUtpsXYA')

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, "<b>Привет, сейчас погода не очень)</b>", parse_mode='html')


@bot.message_handler(content_types=['text'])
def example(message):
    sti = open('sticker.webp', 'rb')

    markip = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    website = types.KeyboardButton('python')
    starter = types.KeyboardButton('Hello')
    ids = types.KeyboardButton('ID')
    names = types.KeyboardButton(message.from_user.first_name)
    sun = types.KeyboardButton('Солнце☀')
    weer = types.KeyboardButton('Погода в Витебске')

    markip.add(website, starter, ids, names, sun, weer)

    if message.text != 'python':
        if message.text != 'Hello':
            if message.text != 'ID':
                if message.text != 'Солнце☀':
                    if message.text != message.from_user.first_name:
                        if message.text != 'Погода в Витебске':
                            bot.send_message(message.chat.id, 'Выбери любую кнопку', reply_markup=markip)

    if message.text == 'python':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посети сайт погоды", url='https://pypi.org/project/pyTelegramBotAPI/'))
        bot.send_message(message.chat.id, f'Посети наш сайт)), {message.from_user.username}', parse_mode='html',
                         reply_markup=markup)

    if message.text == 'Hello':
        bot.send_message(message.chat.id, f'И тебе привет {message.from_user.username}', parse_mode='html')
        bot.send_sticker(message.chat.id, sti)

    if message.text == 'ID':
        bot.reply_to(message, f'Твой ID: {message.from_user.id}', parse_mode='html')

    if message.text == message.from_user.first_name:
        bot.send_message(message.chat.id,
                         f'А к нам зашёл самый красивый и приятный человек, существующий в телеграмме. И это {message.from_user.first_name}',
                         parse_mode='html')

    if message.text == 'Солнце☀':
        bot.send_message(message.chat.id,
                         "Оно выглянит если кто-то улыбнётся и много раз, а то солнце хочет солнца и не вылазит с кровати")

#Бот погоды
    if message.text == 'Погода в Витебске':
        bot.send_message(message.chat.id,f"Осадки: {data['list'][0]['weather'][0]['description']}\n"
                                         f"Температура сейчас: {data['list'][0]['main']['temp']}\u00b0C\n"
                                         f"Ощущается как: {data['list'][0]['main']['feels_like']}\u00b0C\n"
                                         f"Мин. возможная температура: {data['list'][0]['main']['temp_min']}\u00b0C\n"
                                         f"Макс. возможная температура: {data['list'][0]['main']['temp_max']}\u00b0C\n"
                                         f"Видимость: {data['list'][0]['main']['humidity']}%\n"
                                         f"Давление: {data['list'][0]['main']['pressure']}hPa\n"
                                         f"Скорость ветра: {data['list'][0]['wind']['speed']}м/с", parse_mode='html')

bot.polling(none_stop=True)
