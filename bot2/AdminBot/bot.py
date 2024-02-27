from telebot import TeleBot, types
import sqlite3
import datetime
# import pytz

TOKEN = '6815877539:AAGbl4UAI-JTsTDEjxLR88WHuab76rqSEeI'
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hello')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hello')

bot.polling(none_stop=True, interval=0)
