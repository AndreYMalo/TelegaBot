import COVID19Py
import telebot

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1453562215:AAEzET3P8qhTpWM9E7Zz-cFFq-SAKBzCXUs')

@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привет {message.from_user.first_name}!</b>\nВведите страну"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19

bot.polling(none_stop=True)
