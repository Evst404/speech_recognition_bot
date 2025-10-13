from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dialogflow_utils import detect_intent_text
import os


LANGUAGE_CODE = 'RU_RU'


def start(update: Update, context: CallbackContext) -> None:
    session_id = f"tg-{update.effective_user.id}"
    try:
        response = detect_intent_text(project_id, session_id, "привет", LANGUAGE_CODE)
        update.message.reply_text(response['queryResult']['fulfillmentText'])
    except Exception:
        pass 

def process_message(update: Update, context: CallbackContext) -> None:
    session_id = f"tg-{update.effective_user.id}"
    try:
        response = detect_intent_text(project_id, session_id, update.message.text, LANGUAGE_CODE)
        update.message.reply_text(response['queryResult']['fulfillmentText'])
    except Exception:
        pass 


def main():
    from dotenv import load_dotenv
    load_dotenv()
    global project_id
    token = os.environ['TELEGRAM_BOT_TOKEN']
    project_id = os.environ['DIALOGFLOW_PROJECT_ID']
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, process_message))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()