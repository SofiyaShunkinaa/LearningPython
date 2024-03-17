from telebot import TeleBot, types
import telebot
import requests
from bs4 import BeautifulSoup

TOKEN = '7127779338:AAGjrI1qjihYkVsj7NyXTP0f-YOE7bu9a3s'
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'menu'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = (types.InlineKeyboardButton('Погода', callback_data='weather'))
    btn2 = (types.InlineKeyboardButton('Гороскоп', callback_data='horoscope'))
    btn3 = (types.InlineKeyboardButton('Новости', callback_data='news'))
    markup.row(btn1, btn2, btn3)
    bot.reply_to(message, "Привет! Выбери интересующую вас кнопку", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_message(callback):
    if callback.data == 'weather':
        weather(callback.message)
    elif callback.data == 'horoscope':
        horoscope(callback.message)
    elif callback.data == 'news':
        news(callback.message)
    elif callback.data == 'minsk':
        weather_town('https://yandex.by/pogoda/minsk?lat=53.902735&lon=27.555691', callback.message)
    elif callback.data == 'vilnius':
        weather_town('https://yandex.by/pogoda/11475', callback.message)
    elif callback.data == 'warsaw':
        weather_town('https://yandex.by/pogoda/?lat=52.23262405&lon=21.00928497', callback.message)
    elif callback.data == 'mail.ru':
        horoscope_source1('https://horo.mail.ru/prediction/taurus/year/#:~:text=%D0%93%D0%BE%D1%80%D0%BE%D1%81%D0%BA%D0%BE%D0%BF%20%D0%BD%D0%B0%202024%20%D0%B3%D0%BE%D0%B4%3A%20%D0%A2%D0%B5%D0%BB%D0%B5%D1%86&text=%D0%9E%D1%81%D0%BE%D0%B1%D0%B5%D0%BD%D0%BD%D0%BE%20%D1%85%D0%BE%D1%80%D0%BE%D1%88%D0%BE%20%D0%B2%D1%8B%20%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D1%82%D0%B5%D1%81%D1%8C%20%D1%81,%D0%92%D0%B0%D1%81%20%D0%B6%D0%B4%D0%B5%D1%82%20%D0%BF%D0%BB%D0%BE%D0%B4%D0%BE%D1%82%D0%B2%D0%BE%D1%80%D0%BD%D1%8B%D0%B9%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%B5%D1%81%D0%BD%D1%8B%D0%B9%20%D0%B4%D0%B5%D0%BD%D1%8C.', callback.message)
    elif callback.data == 'rambler':
        horoscope_source2('https://horoscopes.rambler.ru/taurus/2024/', callback.message)
    elif callback.data == 'rbk':
        horoscope_source3('https://www.rbc.ru/life/news/657805719a794767420b5240', callback.message)


def weather(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Минск', callback_data='minsk'))
    markup.add(types.InlineKeyboardButton('Вильнюс', callback_data='vilnius'))
    markup.add(types.InlineKeyboardButton('Варшава', callback_data='warsaw'))
    bot.reply_to(message, "Выберите интересующий вас город", reply_markup=markup)


def horoscope(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Гороскоп от mail.ru', callback_data='mail.ru'))
    markup.add(types.InlineKeyboardButton('Гороскоп от Рамблер', callback_data='rambler'))
    markup.add(types.InlineKeyboardButton('Гороскоп от РБК', callback_data='rbk'))
    bot.reply_to(message, "Выберите источник гороскопа для тельца на 2024", reply_markup=markup)


def news(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Новости веб-дизайна', url='https://pentaschool.ru/news/veb-dizajn'))
    markup.add(types.InlineKeyboardButton('Новости веб-разработки', url='https://tproger.ru/tag/web'))
    bot.reply_to(message, "Выберите интересующие вас новости", reply_markup=markup)


def weather_town(url, message):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "html.parser")
    town = bs.find('h1', 'title title_level_1 header-title__title')
    temp = bs.find('span', 'temp__value temp__value_with-unit')

    if town is not None and temp is not None:
        bot.send_message(message.chat.id, 'Погода в '+town.text + ' ' + temp.text)
    else:
        bot.send_message(message.chat.id, "Информация о погоде не найдена")


def horoscope_source1(url, message):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "html.parser")
    text = bs.find('div', 'article__item article__item_alignment_left article__item_html')

    if text is not None:
        bot.send_message(message.chat.id, '**Гороскоп для тельцов 2024 от mail.ru**\n' + text.text)
    else:
        bot.send_message(message.chat.id, "Информация не найдена")


def horoscope_source2(url, message):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "html.parser")
    text = bs.find('p')

    if text is not None:
        bot.send_message(message.chat.id, '**Гороскоп для тельцов 2024 от Рамблер**\n' + text.text)
    else:
        bot.send_message(message.chat.id, "Информация не найдена")


def horoscope_source3(url, message):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "html.parser")
    text = bs.find('div', 'card-wrapper')

    if text is not None:
        bot.send_message(message.chat.id, '**Гороскоп для тельцов 2024 от РБК**\n' + text.text)
    else:
        bot.send_message(message.chat.id, "Информация не найдена")


bot.polling(none_stop=True)
