import os
import logging
from telegram.ext import Updater, MessageHandler, Filters , CommandHandler
from dotenv import load_dotenv
import dialogflow_v2 as dialogflow
import logs

tg_logger = logging.getLogger('telegram')


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Здравствуйте")


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
    telegram_token_bot = os.getenv('TELEGRAM_TOKEN_ACCESS')

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    tg_logger.setLevel(logging.INFO)
    logs.main()

    updater = Updater(telegram_token_bot, use_context=True)
    tg_logger.info('Start telegram_bot')
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()
    tg_logger.info('Telegram bot was down')


if __name__ == '__main__':
    main()
