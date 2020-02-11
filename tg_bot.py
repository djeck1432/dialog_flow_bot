import os
import logging
from telegram.ext import Updater, MessageHandler, Filters , CommandHandler
from dotenv import load_dotenv
from dialogflow_response import detect_intent_texts
import logs

logger = logging.getLogger('telegram_logs')


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Здравствуйте")


def get_response(update, context):
    dialogflow_response = detect_intent_texts('massive-sandbox-266519', '1234', update.message.text, 'ru')
    update.message.reply_text(dialogflow_response)


def main():
    load_dotenv()
    telegram_bot_token = os.getenv('TELEGRAM_ACCESS_TOKEN')
    telegram_logs_token = os.getenv('TELEGRAM_LOG_BOT_TOKEN')
    telegram_log_chat_id = os.getenv('TELEGRAM_LOG_BOT_CHAT_ID')

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger.setLevel(logging.INFO)
    logs.create_bot_handler(telegram_logs_token, telegram_log_chat_id)

    updater = Updater(telegram_bot_token, use_context=True)
    logger.info('Start telegram_bot')
    updater.dispatcher.add_handler(MessageHandler(Filters.text, get_response))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()
    logger.info('Telegram bot was down')


if __name__ == '__main__':
    main()
