import telebot

bot = telebot.TeleBot('5712089533:AAEi2SsohjvTFjenc80lO2lzjQzTeHSXwVM')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здарова {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)

bot.polling(none_stop=True)