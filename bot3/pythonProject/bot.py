from telebot import TeleBot, types
import telebot

TOKEN = '7127779338:AAGjrI1qjihYkVsj7NyXTP0f-YOE7bu9a3s'
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
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


def weather(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Минск', callback_data='minsk'))
    markup.add(types.InlineKeyboardButton('Вильнюс', callback_data='vilnius'))
    markup.add(types.InlineKeyboardButton('Варшава', callback_data='warsaw'))
    bot.reply_to(message, "Выберите интересующий вас город", reply_markup=markup)


def horoscope(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Гороскоп от mail.ru', callback_data='minsk'))
    markup.add(types.InlineKeyboardButton('Гороскоп от КП', callback_data='vilnius'))
    markup.add(types.InlineKeyboardButton('Гороскоп от РБК', callback_data='warsaw'))
    bot.reply_to(message, "Выберите источник гороскопа для тельца на 2024", reply_markup=markup)


def news(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Новости веб-дизайна', url='https://pentaschool.ru/news/veb-dizajn'))
    markup.add(types.InlineKeyboardButton('Новости веб-разработки', url='https://tproger.ru/tag/web'))
    bot.reply_to(message, "Выберите интересующие вас новости", reply_markup=markup)


bot.polling(none_stop=True)
