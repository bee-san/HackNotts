from telegram.ext import MessageHandler, Filters 
from telegram.ext import Updater, CommandHandler
import requests
import telegramToken

updater = Updater(token= telegramToken.token, use_context=True)
wit = "https://api.wit.ai/message"


dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm brandonBot.")

def get_url():
    url = requests.request("GET", "http://api.giphy.com/v1/gifs/random", params={"api_key":"pgHiOtZymIiPTrEgdYWqqYav1eSjOIgR","rating":"PG-13"}).json()
    return url['data']['images']['original']['url']

def photo(update, context):
    url = get_url()
    chat_id = update.effective_chat.id
    context.bot.send_animation(chat_id=chat_id, animation=url)
    
def echo(update, context):
    txt = update.message.text
    querystring = {"v":"20191117","q":txt}
    
    headers = {
        'Authorization': "Bearer O22LR566VRN74YN7FLOVI3NADYISG4SO",
        'cache-control': "no-cache",
        'Postman-Token': "8dc65357-32b6-4252-81ec-224fc7a1165e"
    }
    response = requests.request("GET", wit, headers=headers, params=querystring).json()
    print(response['entities']['intent'][0]['value'])    
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)
    
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
