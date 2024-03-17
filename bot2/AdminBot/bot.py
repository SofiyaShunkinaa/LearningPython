from telebot import TeleBot, types
import sqlite3
import datetime
# import pytz

TOKEN = '6815877539:AAGbl4UAI-JTsTDEjxLR88WHuab76rqSEeI'
bot = TeleBot(TOKEN)

conn = sqlite3.connect('fidel.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS services (id INTEGER PRIMARY KEY, name VARCHAR(255), date DATE)')
cur.execute('CREATE TABLE IF NOT EXISTS bookings (id INTEGER PRIMARY KEY, name VARCHAR(50), phone VARCHAR(50), ')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, '''
    Чтобы записаться выбери 
    ''')


@bot.message_handler(commands=['Записаться'])
def send_welcome(message):


bot.polling(none_stop=True, interval=0)
