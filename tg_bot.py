import os
import logging
from telegram.ext import Updater, MessageHandler, Filters , CommandHandler
from dotenv import load_dotenv
from dialogflow_response import detect_intent_texts
import logs

tg_logger = logging.getLogger('telegram')


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Здравствуйте")


def get_response(update, context):
    dialogflow_response = detect_intent_texts('massive-sandbox-266519', '1234', update.message.text, 'ru')
    update.message.reply_text(dialogflow_response)


def main():
    load_dotenv()
    token_bot_telegram = os.getenv('TOKEN_ACCESS_TELEGRAM')

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    tg_logger.setLevel(logging.INFO)
    logs.main()

    updater = Updater(token_bot_telegram, use_context=True)
    tg_logger.info('Start telegram_bot')
    updater.dispatcher.add_handler(MessageHandler(Filters.text, get_response))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()
    tg_logger.info('Telegram bot was down')


if __name__ == '__main__':
    main()
