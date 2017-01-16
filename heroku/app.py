# -*- coding: utf-8 -*-
import telebot
import os
from flask import Flask, request
from config import agunda_token
from config import agunda_botan_key
import config
import requests
import botan

bot = telebot.TeleBot(agunda_token)

server = Flask(__name__)


@bot.message_handler(commands=['start'])
def echo_message(message):
    bot.send_message(message.chat.id, 'меню', reply_markup=config.mainmenu)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    if message.text.lower() in ['байрай', 'салам', 'da bon horz', 'salam', 'bairai', 'агас цу']:
        bot.reply_to(message, 'Da bon horz, ' + message.from_user.first_name)
    elif message.text in ['Меню', 'меню', 'Фæстæмæ (назад)', 'фæстæмæ (назад)']:
        bot.send_message(message.chat.id, 'меню', reply_markup=config.mainmenu)

    elif message.text == 'Мæн тыххай👼':
        bot.send_message(message.chat.id, config.iron_description)
    elif message.text == 'Обо мне':
        bot.send_message(message.chat.id, config.rus_description)
    elif message.text == config.s + 'боныхъæд абон (погода сегодня)':
        bot.send_message(message.chat.id, 'кацы горат', reply_markup=config.weathertoday)
    elif message.text == config.s + 'боныхъæд 5 боны (на 5 дней)':
        bot.send_message(message.chat.id, 'равзар да горæт', reply_markup=config.weatherforecast)

    elif message.text in config.wtd:
        bot.send_message(message.chat.id, config.weatherCurrentFun(config.wtd[message.text]), parse_mode='HTML')
        botan.track(config.allon_botan_key, message.chat.id, message, 'weathertoday')
    elif message.text in config.wfd:
        bot.send_message(message.chat.id,
                         config.weatherForecastFun(config.getFiveDaysWeather(config.wfd[message.text])),
                         parse_mode='HTML')
        botan.track(config.allon_botan_key, message.chat.id, message, 'weatherforecast')


    else:
        if config.getresponse(message.text)[1:18] == 'нæма зонын тæлмац':
            for i in message.text.split(' '):
                bot.send_message(message.chat.id, config.getresponse(i))
        else:
            bot.send_message(message.chat.id, config.getresponse(message.text))
        botan.track(config.agunda_botan_key, message.chat.id, message, 'translate')



	
	
	
	
# bot.remove_webhook()
# bot.polling()


@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://agunda.herokuapp.com/bot")
    return "!", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
server = Flask(__name__)


