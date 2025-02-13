from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os
from dotenv import load_dotenv
from functions import find_words
load_dotenv()
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Отправьте мне слово и я выведу слова, которые можно из него составить")

def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    result = find_words(user_message)
    update.message.reply_text(f"Вот {len(result)} Слов из слова {user_message}: {', '.join(result)}")

def main():
    TOKEN = os.getenv('TOKEN')

    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()