from jinja2 import pass_eval_context
import Constants
from telegram import Update
from telegram.ext import *


def start_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hey, ask me anything")


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("I am a bot created by Maor Sabag for the sake of Python testing")
    

def error(update, context):
    print(f"Update {update} has caused error {context.error}")


def main():
    print("Bot has started....")
    updater = Updater(Constants.API_KEY)
    dp = updater.dispatcher # Dispatcher

    dp.add_handler(CommandHandler("start"), start_command)
    dp.add_handler(CommandHandler("help"), help_command)
    # dp.add_handler(MessageHandler(Filters.text))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
    
    
if __name__ == '__main__':
    main()