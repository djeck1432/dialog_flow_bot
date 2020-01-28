import os
import telegram
import logging
from telegram.ext import Updater, MessageHandler, Filters
from dotenv import load_dotenv
import dialogflow_v2 as dialogflow


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def echo(update, context):
    dialogflow_response = detect_intent_texts('massive-sandbox-266519', '1234', update.message.text, 'ru')
    update.message.reply_text(dialogflow_response)


def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input)
    return response.query_result.fulfillment_text

def main():
    load_dotenv()
    telegram_access_token = os.getenv('TELEGRAM_TOKEN_ACCESS')
    updater = Updater(telegram_access_token, use_context=True)

    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
    updater.dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
