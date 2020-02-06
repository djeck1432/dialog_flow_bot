import logging
import os
import telegram
from dotenv import load_dotenv


class TelegramLogsHandler(logging.Handler):
    def __init__(self, telegram_log_access_token, telegram_log_chat_id):
        logging.Handler.__init__(self)
        self.telegram_access_token = telegram_log_access_token
        self.telegram_log_chat_id = telegram_log_chat_id
        self.bot_log = telegram.Bot(token=telegram_log_access_token )

    def emit(self, record):
        log_entry = self.format(record)
        return self.bot_log.send_message(chat_id=self.telegram_log_chat_id, text=log_entry)


def main():
    load_dotenv()
    telegram_logs_token = os.getenv('TELEGRAM_LOG_BOT_TOKEN')
    telegram_logs_chat_id = os.getenv('TELEGRAM_LOG_BOT_CHAT_ID')
    bot = TelegramLogsHandler(telegram_logs_token,telegram_logs_chat_id)

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    tg_logger = logging.getLogger('telegram')
    tg_logger.addHandler(bot)

    vk_logger = logging.getLogger('vk_bot')
    vk_logger.addHandler(bot)


if __name__ == '__main__':
    main()
