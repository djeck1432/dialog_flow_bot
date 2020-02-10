import logging
import os
import telegram
from dotenv import load_dotenv
from tg_bot import tg_logger
from vk_bot import vk_logger


class TelegramLogsHandler(logging.Handler):

    def __init__(self, bot_log, log_chat_id_telegram):
        super().__init__()
        self.log_chat_id_telegram = log_chat_id_telegram
        self.bot_log = bot_log


    def emit(self, record):
        log_entry = self.format(record)
        self.bot_log.send_message(chat_id=self.log_chat_id_telegram, text=log_entry)

def main():
    load_dotenv()
    logs_token_telegram = os.getenv('TOKEN_LOG_BOT_TELEGRAM')
    log_chat_id_telegram = os.getenv('LOG_BOT_CHAT_ID_TELEGRAM')
    bot_log = telegram.Bot(token=logs_token_telegram)

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    tg_logger.setLevel(logging.INFO)
    tg_logger.addHandler(TelegramLogsHandler(bot_log,log_chat_id_telegram))
    vk_logger.setLevel(logging.INFO)
    vk_logger.addHandler(TelegramLogsHandler(bot_log,log_chat_id_telegram))


if __name__ == '__main__':
    main()
