# Author code: mython-dev or myth-dev
# Instagram: @mython_dev or h4ckerworld
# Telegram: @myth_dev
# GitHub: https://github.com/mython_dev

# Да есть Баги.... :(



from telebot import *
import pytube
from buttons import *
import os
import random
import time



TOKEN = '5438670868:AAG059x3oIPcxGQODCsziJG9xJiPx5vogMM'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])

def start_message(message):
  bot.send_message(message.chat.id,"Выберите от куда вы хотите скачать видео.", reply_markup = social_network)



@bot.callback_query_handler(func=lambda call: True)

def choose_social_network(call):
  if call.data == 'INS':
        bot.send_message(call.message.chat.id, 'Пока не Работает:(')

  elif call.data == 'YT':
      bot.send_message(call.message.chat.id, '👋 Пришлите ссылку на YouTube видео и я его скачаю для вас ❤️‍🔥')


      @bot.message_handler()

      def YOUTUBE_DOWNLOADER(message):

        link = message.text
 
        yt = pytube.YouTube(link)

  
        bot.send_message(message.chat.id, 'Попробую  это скачать...')

        
        file = yt.streams.filter(progressive=True, file_extension="mp4")

        file.get_highest_resolution().download()

           
        finally_name = ''.join((random.choice('qwertyuiopasdfghjklzxcvbnm')for i in range(6)))

        os.rename(file, finally_name)

        video = open(finally_name, 'rb')


        bot.reply_to(message, 'Отправляю.... Ждите')

        
        bot.send_video(message.chat.id, video, caption='Cкачано с помощью @myth_downloader_ytbot')

        time.sleep(5)

        os.remove(finally_name)

# @bot.message_handler(content_types=['text'])


# def get_text_messages(message):

#    bot.send_message(message.chat.id, 'test')
           
bot.infinity_polling()