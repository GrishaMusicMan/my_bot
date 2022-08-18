import telebot
from telebot import  types
import random

bot = telebot.TeleBot('5712089533:AAEi2SsohjvTFjenc80lO2lzjQzTeHSXwVM')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здарова {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)

# @bot.message_handler(content_types=['text'])
# def get_message(message):
#     if message.text == "Привет":
#         bot.send_message(message.chat.id, 'И тебе Привет!')
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f'Твой id: {message.from_user.id}')
#     elif message.text == "photo":
#         photo = open('Mybot.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     elif message.text == "Скинь мне крутой трек":
#         audio = open('Oxxxymiron - Агент.mp3', 'rb')
#         bot.send_audio(message.chat.id, audio)

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    vau = ['Круто!!!', 'Cool!!!', 'Мать моя женщина!']
    bot.send_message(message.chat.id, vau[random.randint(0, 2)])

@bot.message_handler(commands=['footbal'])
def footbal(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Сайт Английского футбола", url='http://fapl.ru/'))
    bot.send_message(message.chat.id, "Новости футбола", reply_markup=markup)

@bot.message_handler(commands=['menu'])
def footbal(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    open = types.KeyboardButton('open')
    close = types.KeyboardButton('close')
    settings = types.KeyboardButton('settings')

    markup.add(open, close, settings)
    bot.send_message(message.chat.id, "Кнопочки", reply_markup=markup)


bot.polling(none_stop=True)