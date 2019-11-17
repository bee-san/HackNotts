"""
The Telegram bot client
"""

import requests

from bs4 import BeautifulSoup
import time
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re 


token =  "1019752473:AAEzlIeStcZB25djykEjNJLQzVlyVn8p7YU"


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def getChatID(bot, update):
    chat_id = update.message.chat_id
    txt = f"The exact chat ID is \"{chat_id}\" and the type is {type(chat_id)}"
    bot.send_message(chat_id=chat_id, text=txt)

def bop(bot, update):
    print("running bop")
    url = get_url()
    chat_id = update.message.chat_id
    # chat_id = 749894187
    
    bot.send_photo(chat_id=chat_id, photo=url)

def check(bot, update):
    chat_id = update.message.chat_id
    ret = blog.checkBadWords()

    bot.send_message(chat_id=749894187, text=ret)

def check404(bot, update):
    chat_id = update.message.chat_id
    ret = blog.check404Links()
    bot.send_message(chat_id=749894187, text=ret)

def views(bot, update):
    chat_id = update.message.chat_id
    ret = str(blog.getAnalytics())
    bot.send_message(chat_id=749894187, text=ret)


def doall(bot, update):
    ret = blog.report()
    bot.send_message(chat_id=749894187, text=ret)

def logs(bot, update):
    file = open("crontabs/blog_checker.log")
    f = file.read()
    file.close()
    bot.send_message(chat_id=749894187, text=f)
                

def main():
    updater = Updater('1019752473:AAEzlIeStcZB25djykEjNJLQzVlyVn8p7YU')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(CommandHandler('doall',doall))
    dp.add_handler(CommandHandler('check',check))
    dp.add_handler(CommandHandler('404',check404))
    dp.add_handler(CommandHandler('views',views))
    dp.add_handler(CommandHandler('chat',getChatID))
    dp.add_handler(CommandHandler('logs',logs))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
