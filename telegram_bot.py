from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from google.cloud import dialogflow
from google.protobuf.json_format import MessageToDict
from dotenv import load_dotenv
import os


load_dotenv()

project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
language_code = 'ru-RU'


def detect_intent_text(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(request={"session": session, "query_input": query_input})
    return MessageToDict(response._pb)


def start(update: Update, context: CallbackContext) -> None:
    session_id = str(update.effective_user.id)
    response = detect_intent_text(project_id, session_id, "привет", language_code)
    update.message.reply_text(response['queryResult']['fulfillmentText'])


def echo(update: Update, context: CallbackContext) -> None:
    session_id = str(update.effective_user.id)
    response = detect_intent_text(project_id, session_id, update.message.text, language_code)
    update.message.reply_text(response['queryResult']['fulfillmentText'])


def main() -> None:
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()