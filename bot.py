from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token=os.environ['BOTTOKEN'], use_context=True)

dispatcher = updater.dispatcher

message_ids = []

def handle_start(update, context):
    message_ids.append(update.message.message_id)
    message = context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Here you would get financial info...")
    message_ids.append(message.message_id)

def handle_help(update, context):
    message_ids.append(update.message.message_id)
    message = context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Right now I can only receive messages and echo them back to you")
    message_ids.append(message.message_id)

def handle_clear(update, context):
    message_ids.append(update.message.message_id)
    for message_id in message_ids:
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=message_id)
    message_ids.clear()

def handle_echo(update, context):
    print(update.message.text)
    message_ids.append(update.message.message_id)
    message = context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    message_ids.append(message.message_id)

start_handler = CommandHandler('start', handle_start)
help_handler = CommandHandler('help', handle_help)
clear_handler = CommandHandler('clear', handle_clear)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(clear_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), handle_echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
