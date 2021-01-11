import os
import config
import telebot
import scrapping

# /start, /help and etc
bot = telebot.TeleBot(config.token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Smth will be here')

#Reply same msg on every text
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, 'Попизди мне тут')

'''
#Forward all incoming messages to #Userid
@bot.message_handler(func=lambda message: True)
def forward_to_admin(message):
    bot.send_message(config.adminid, message, disable_notifications)
'''

bot.polling()


map = dict()
map['web'] = 116
