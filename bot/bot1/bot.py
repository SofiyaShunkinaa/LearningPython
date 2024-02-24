from telebot import TeleBot, types
import sqlite3
import datetime
import traceback

TOKEN = '6413161576:AAGcUNYAFO1BZu6Ja0pXz4VcB8yC-XUlJ-w'
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    try:
        bot.send_message(message.chat.id, 'привет suchka 🥰')
        conn = sqlite3.connect('bot.db')
        cur = conn.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50), count INTEGER)')
        conn.commit()
        bot.send_message(message.chat.id, 'сейчас тебя зарегистрируем... Укажи твой текущий счёт')
        bot.register_next_step_handler(message, user_count)
    except Exception as e:
        print('Ошибка в start:\n', traceback.format_exc())
        bot.send_message(message.chat.id, f'Ошибка в start: {traceback.format_exc()}')
    finally:
        cur.close()
        conn.close()


def user_count(message):
    try:
        count = message.text.strip()
        conn = sqlite3.connect('bot.db')
        cur = conn.cursor()

        cur.execute('SELECT * FROM users')
        users = cur.fetchall()

        check = 0
        for user in users:
            if message.from_user.first_name == user[1]:
                check = 1

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Помощь')
        btn4 = types.KeyboardButton(text='Статистика')
        markup.add(btn1, btn4)
        btn2 = types.KeyboardButton(text='Я спать 😴')
        btn3 = types.KeyboardButton(text='Я проебалась')
        markup.add(btn2, btn3)

        if check == 0:
            cur.execute("INSERT INTO users (name, count) VALUES ('%s', '%s')" % (message.from_user.first_name, count))
            conn.commit()
            bot.send_message(message.chat.id, 'Отлично, ты в базе!', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'похоже, ты уже есть в базе, так что не пизди', reply_markup=markup)
        bot.register_next_step_handler(message, on_click)
    except Exception as e:
        print('Ошибка в user_count:\n', traceback.format_exc())
        bot.send_message(message.chat.id, f'Ошибка в user_count: {traceback.format_exc()}')
    finally:
        cur.close()
        conn.close()


def on_click(message):
    try:
        if message.text == "Помощь" or message.text == "/help":
            help(message)
            bot.register_next_step_handler(message, on_click)
        elif message.text == "Статистика":
            statistics(message)
            bot.register_next_step_handler(message, on_click)
        elif message.text == "Я спать 😴" or message.text == "Я проебалась":
            sleep(message)
            bot.register_next_step_handler(message, on_click)
        else:
            bot.register_next_step_handler(message, on_click)
    except Exception as e:
        print('Ошибка в on_click:\n', traceback.format_exc())
        bot.send_message(message.chat.id, f'Ошибка в on_click: {traceback.format_exc()}')


@bot.message_handler(commands=['help'])
def help(message):
    try:
        bot.send_message(message.chat.id, 'пошла нахуй!!!')
    except Exception as e:
        print('Ошибка в help:\n', traceback.format_exc())
        bot.send_message(message.chat.id, f'Ошибка в help: {traceback.format_exc()}')


@bot.message_handler(func=lambda message: True)
def sleep(message):
    try:
        message_time = datetime.datetime.fromtimestamp(message.date)
        message_hour = message_time.hour + 3
        message_minute = message_time.minute
        if message_minute >= 10:
            bot.send_message(message.chat.id, f'Ваше время: {message_hour}:{message_minute}')
        else:
            bot.send_message(message.chat.id, f'Ваше время: {message_hour}:0{message_minute}')

        conn = sqlite3.connect('bot.db')
        cur = conn.cursor()

        if message_hour in [20, 21, 22, 23, 0]:
            message_hour = 0
            bot.send_message(message.chat.id, "Спокойной ночи!✨✨✨")
        elif message_hour == 1:
            bot.send_message(message.chat.id, "Тебе +1\nСпокойной ночи!✨✨✨")
        elif message_hour == 2:
            bot.send_message(message.chat.id, "Тебе +2\nСпокойной ночи!✨✨✨")
        elif message_hour == 3:
            bot.send_message(message.chat.id, "Тебе +3\nСпокойной ночи!✨✨✨")
        elif message_hour == 4:
            bot.send_message(message.chat.id, "Тебе +4\nСпокойной ночи!✨✨✨")
        else:
            message_hour = 0
            bot.send_message(message.chat.id, "Ещё не время спать!")

        cur.execute("UPDATE users SET count = count + '%s' WHERE name = '%s'" % (message_hour, message.from_user.first_name))
        conn.commit()
    except Exception as e:
        print('Ошибка в sleep:\n', traceback.format_exc())
        bot.send_message(message.chat.id, f'Ошибка в sleep: {traceback.format_exc()}')
    finally:
        cur.close()
        conn.close()


@bot.message_handler(commands=['statistics'])
def statistics(message):
    try:
        conn = sqlite3.connect('bot.db')
        cur = conn.cursor()

        cur.execute('SELECT * FROM users')
        users = cur.fetchall()

        data = ''
        for user in users:
            data += f'<b>{user[1]}</b>: {user[2]}\n'
        bot.send_message(message.chat.id, data, parse_mode='html')
    except Exception as e:
        print('Ошибка в statistics:\n', traceback.format_exc())
        bot.send_message(message.chat.id, f'Ошибка в statistics: {traceback.format_exc()}')
    finally:
        cur.close()
        conn.close()


bot.polling(none_stop=True, interval=0)