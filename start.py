from telegram.ext import MessageHandler, Filters 
from telegram.ext import Updater, CommandHandler
import requests
updater = Updater(token='1019752473:AAEzlIeStcZB25djykEjNJLQzVlyVn8p7YU', use_context=True)


dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def get_url():
    url = requests.request("GET", "http://api.giphy.com/v1/gifs/random", params={"api_key":"pgHiOtZymIiPTrEgdYWqqYav1eSjOIgR","rating":"PG-13"}).json()
    return url['data']['images']['original']['url']

def photo(update, context):
    url = get_url()
    chat_id = update.effective_chat.id
    context.bot.send_animation(chat_id=chat_id, animation=url)
    
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    
def getChatID(update, context):
    #context.bot.send_message(chat_id=update.effective_chat.id, text="I'm another bot, please talk to me!")
    chat_id = update.effective_chat.id
    txt = f"The exact chat ID is \"{chat_id}\" and the type is {type(chat_id)}"
    context.bot.send_message(chat_id=chat_id, text=txt)

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
chat_handler = CommandHandler('chat', getChatID)
dispatcher.add_handler(chat_handler)
photo_handler = CommandHandler('photo', photo)
dispatcher.add_handler(photo_handler)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)   

updater.start_polling()

def main():
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
