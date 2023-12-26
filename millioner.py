import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Text
import requests

logging.basicConfig(level=logging.INFO)

bot = Bot(token='1120486477:AAFJhpujfVdsEftw8HHo8CvGgrITUtpsXYA')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    kb = [[types.KeyboardButton(text="Погода"),
           types.KeyboardButton(text="Игры")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer_sticker('CAACAgIAAxkBAAIFqmQyntNSGBMHWfdaIsqG3hqYZLEnAALfBQAC6wNNAAGmG3B7cP-YvS8E')
    await message.answer("Пока проба всего деяния", reply_markup=keyboard)


@dp.message_handler(Text('Игры'))
async def welcome(message: types.Message):
    kb = [[types.KeyboardButton(text="21"),
           types.KeyboardButton(text="Миллионер")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("О, вы выбрали игры. Какую вам?)", reply_markup=keyboard)


@dp.message_handler(Text('Миллионер'))
async def welcome(message: types.Message):
    kb = [[types.KeyboardButton(text="А. Коммивояжером"),
           types.KeyboardButton(text="Б. Местным шерифом")],
          [types.KeyboardButton(text='В. Его зубным врачом'),
           types.KeyboardButton(text='Г. Его мясником')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(f"Хорошо. Начнём.\nКем был мужчина, послуживший моделью "
                         f"для известной картины «Американская готика» Гранта Вуда?)", reply_markup=keyboard)


@dp.message_handler(content_types='text')
async def game(message: types.Message):
    kb3 = [[types.KeyboardButton(text="А. Гугол"),
            types.KeyboardButton(text="Б. Мегатрон")],
           [types.KeyboardButton(text='В. Гигабит'),
            types.KeyboardButton(text='Г. Наномоль')]]
    keyboard3 = types.ReplyKeyboardMarkup(keyboard=kb3, resize_keyboard=True)
    kb2 = [[types.KeyboardButton(text="А. Ананас"),
            types.KeyboardButton(text="Б. Вишня")],
           [types.KeyboardButton(text='В. Кокос'),
            types.KeyboardButton(text='Г. Абрикос')]]
    keyboard2 = types.ReplyKeyboardMarkup(keyboard=kb2, resize_keyboard=True)
    kb1 = [[types.KeyboardButton(text="А. Мотылек"),
            types.KeyboardButton(text="Б. Таракан")],
           [types.KeyboardButton(text='В. Муха'),
            types.KeyboardButton(text='Г. Японский хрущик')]]
    keyboard1 = types.ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    kb = [[types.KeyboardButton(text="21"),
           types.KeyboardButton(text="Миллионер")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    if message.text == 'В. Его зубным врачом':
        await message.answer(f'Верно.\nУ вас 1000 очков. Следующий вопрос.\n'
                             f'Какое насекомое вызвало короткое замыкание в ранней версии вычислительной машины, '
                             f'тем самым породив термин «компьютерный баг» («баг» в переводе с англ. «насекомое»)?',
                             reply_markup=keyboard1)
    elif message.text == 'А. Коммивояжером':
        await message.answer(f'Увы, но вы проиграли\nНе расстраивайся\nВо что сыграете', reply_markup=keyboard)
    elif message.text == 'Б. Местным шерифом':
        await message.answer(f'Увы, но вы проиграли\nНе расстраивайся\nВо что сыграете', reply_markup=keyboard)
    elif message.text == 'Г. Его мясником':
        await message.answer(f'Увы, но вы проиграли\nНе расстраивайся\nВо что сыграете', reply_markup=keyboard)

    if message.text == 'А. Мотылек':
        await message.answer(f'Верно.\nУ вас 2000 очков. Следующий вопрос.\n'
                             f'Из каких плодов можно получить копру?',
                             reply_markup=keyboard2)
    elif message.text == 'Б. Таракан':
        await message.answer(f'Увы, но вы проиграли\nНе расстраивайся\nВо что сыграете', reply_markup=keyboard)
    elif message.text == 'В. Муха':
        await message.answer(f'Увы, но вы проиграли\nНе расстраивайся\nВо что сыграете', reply_markup=keyboard)
    elif message.text == 'Г. Японский хрущик':
        await message.answer(f'Увы, но вы проиграли\nНе расстраивайся\nВо что сыграете', reply_markup=keyboard)

    if message.text == 'В. Кокос':
        await message.answer(f'Верно.\nУ вас 5000 очков. Следующий вопрос.\n'
                             f'Под каким названием известна единица с последующими ста нулями?',
                             reply_markup=keyboard3)
    elif message.text == 'А. Ананас':
        await message.answer(f'Увы, но вы проиграли\nНе расстраивайся\nВо что сыграете', reply_markup=keyboard)
    elif message.text == 'Б. Вишня':
        await message.answer(f'Увы, но вы проиграли\nНе расстраивайся\nВо что сыграете', reply_markup=keyboard)
    elif message.text == 'Г. Абрикос':
        await message.answer(f'Увы, но вы проиграли\nНе расстраивайся\nВо что сыграете', reply_markup=keyboard)

    if message.text == 'А. Гугол':
        await message.answer(f'Верно.\nУ вас 10000 очков. Следующий вопрос.\n'
                             f'Какой химический элемент составляет более половины массы тела человека?',
                             reply_markup=keyboard2)
    elif message.text == 'Б. Мегатрон':
        await message.answer(f'Увы, но вы проиграли\nНе расстраивайся\nВо что сыграете', reply_markup=keyboard)
    elif message.text == 'В. Гигабит':
        await message.answer(f'Увы, но вы проиграли\nНе расстраивайся\nВо что сыграете', reply_markup=keyboard)
    elif message.text == 'Г. Наномоль':
        await message.answer(f'Увы, но вы проиграли\nНе расстраивайся\nВо что сыграете', reply_markup=keyboard)


# @dp.message_handler(content_types='sticker')
# async def sti(message: types.Message):
#    await message.answer(message.sticker.file_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
