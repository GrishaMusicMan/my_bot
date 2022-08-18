import telebot

bot = telebot.TeleBot('5712089533:AAEi2SsohjvTFjenc80lO2lzjQzTeHSXwVM')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здарова {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)

@bot.message_handler()
def get_message(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, 'И тебе Привет!')
    elif message.text == "id":
        bot.send_message(message.chat.id, f'Твой id: {message.from_user.id}')
    elif message.text == "photo":
        photo = open('Mybot.png', 'rb')
        bot.send_photo(message.chat.id, photo)







bot.polling(none_stop=True)