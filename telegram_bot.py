from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dialogflow_utils import detect_intent_text
import os
from dotenv import load_dotenv


LANGUAGE_CODE = 'RU_RU'


def start(update: Update, context: CallbackContext, project_id: str) -> None:
    session_id = f"tg-{update.effective_user.id}"
    response = detect_intent_text(project_id, session_id, "привет", LANGUAGE_CODE)
    update.message.reply_text(response['queryResult']['fulfillmentText'])


def process_message(update: Update, context: CallbackContext, project_id: str) -> None:
    session_id = f"tg-{update.effective_user.id}"
    response = detect_intent_text(project_id, session_id, update.message.text, LANGUAGE_CODE)
    update.message.reply_text(response['queryResult']['fulfillmentText'])


def main():
    load_dotenv()
    token = os.environ['TELEGRAM_BOT_TOKEN']
    project_id = os.environ['DIALOGFLOW_PROJECT_ID']
    
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler('start', lambda u, c: start(u, c, project_id)))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, lambda u, c: process_message(u, c, project_id)))
    
    try:
        updater.start_polling()
        updater.idle()
    except Exception as e:
        print(f"Ошибка в работе Telegram бота: {e}")
        raise


if __name__ == '__main__':
    main()