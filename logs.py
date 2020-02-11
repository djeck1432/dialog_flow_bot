import logging
import os
import telegram
from dotenv import load_dotenv


class TelegramLogsHandler(logging.Handler):

    def __init__(self, bot_log, telegram_log_chat_id):
        super().__init__()
        self.telegram_log_chat_id = telegram_log_chat_id
        self.bot_log = bot_log

    def emit(self, record):
        log_entry = self.format(record)
        self.bot_log.send_message(chat_id=self.telegram_log_chat_id, text=log_entry)


def main():
    load_dotenv()
    telegram_logs_token = os.getenv('TELEGRAM_LOG_BOT_TOKEN')
    telegram_log_chat_id = os.getenv('TELEGRAM_LOG_BOT_CHAT_ID')
    bot_log = telegram.Bot(token=telegram_logs_token)

    logger = logging.getLogger('bot_logs')
    logger.addHandler(TelegramLogsHandler(bot_log, telegram_log_chat_id))


if __name__ == '__main__':
    main()
