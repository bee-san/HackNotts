from telegram.ext import MessageHandler, Filters 
from telegram.ext import Updater, CommandHandler
import requests
import telegramToken
import banking

updater = Updater(token= telegramToken.token, use_context=True)
wit = "https://api.wit.ai/message"

dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm brandonBot.")

def get_url(tag):
    url = requests.request("GET", "http://api.giphy.com/v1/gifs/random", params={"api_key":"pgHiOtZymIiPTrEgdYWqqYav1eSjOIgR","rating":"PG-13", "tag":{tag, "money"}}).json()
    return url['data']['images']['original']['url']

def gif(update, context, tag):
    url = get_url(tag)
    chat_id = update.effective_chat.id
    context.bot.send_animation(chat_id=chat_id, animation=url)
  
def get_meaning(update, context):
    txt = update.message.text
    querystring = {"v":"20191117","q":txt}
    
    headers = {
        'Authorization': "Bearer O22LR566VRN74YN7FLOVI3NADYISG4SO",
        'cache-control': "no-cache",
        'Postman-Token': "8dc65357-32b6-4252-81ec-224fc7a1165e"
    }
    response = requests.request("GET", wit, headers=headers, params=querystring).json()
    return next(iter(response['entities']))
    
def echo(update, context):
    meaning = get_meaning(update, context)
    print(meaning)
    if (meaning == "intent"):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Your balance is " + str(banking.get_balance(banking.uid)))
    if (meaning == "average_paying"):
        result = banking.assess_last_transaction(banking.uid, banking.category, banking.last)
        if (result[1] == "IN"):
            gif(update, context, "good")
        else:
            gif(update, context, "bad")
        context.bot.send_message(chat_id=update.effective_chat.id, text=banking.assess_last_transaction(banking.uid, banking.category, banking.last))
    if (meaning == "last_transaction"):
        result = banking.get_last_transaction_from_feed(banking.uid, banking.category)
        if (result["direction"] == "IN"):
            gif(update, context, "good")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Your last transaction was inbound, whoooo!")
        else:
            gif(update, context, "bad")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Your last transaction was outbound. Crap.")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
photo_handler = CommandHandler('gif', gif)
dispatcher.add_handler(photo_handler)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)   

updater.start_polling()

def main():
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
