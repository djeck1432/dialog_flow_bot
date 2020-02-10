import os
import logging
from dotenv import load_dotenv
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
from dialogflow_response import detect_intent_texts
import logs


vk_logger = logging.getLogger('vk_bot')


def get_response(event, vk):
    vk.messages.send(
        user_id=event.user_id,
        message=detect_intent_texts('massive-sandbox-266519', '1234', event.text, 'ru'),
        random_id=randint(1, 1000),
    )


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    vk_logger.setLevel(logging.INFO)
    logs.main()

    load_dotenv()
    token_vk = os.getenv('TOKEN_ACCESS_VK')
    vk_session = vk_api.VkApi(token=token_vk)
    vk = vk_session.get_api()
    vk_logger.info('Start VK Bot')
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            if detect_intent_texts('massive-sandbox-266519', '1234', event.text, 'ru') is not None:
                get_response(event, vk)

    vk_logger.critical('Vk bot was down')




if __name__ == '__main__':
    main()
