import os
import logging
from dotenv import load_dotenv
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
import dialogflow_v2 as dialogflow
import logs


vk_logger = logging.getLogger('vk_bot')

def echo(event,vk):
    # vk_logger.info('start')
    vk.messages.send(
        user_id=event.user_id,
        message=detect_intent_texts('massive-sandbox-266519', '1234', event.text, 'ru'),
        random_id=randint(1, 1000),
    )

def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(
        session=session, query_input=query_input)
    if not response.query_result.intent.is_fallback:
        return response.query_result.fulfillment_text



def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    vk_logger.setLevel(logging.INFO)
    logs.main()

    load_dotenv()
    vk_token = os.getenv('VK_TOKEN_ACCESS')
    vk_session = vk_api.VkApi(token=vk_token)
    vk = vk_session.get_api()
    vk_logger.info('Start')
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            if detect_intent_texts('massive-sandbox-266519', '1234', event.text, 'ru') is not None:
                echo(event, vk)

    vk_logger.critical('bot was down')




if __name__ == '__main__':
    main()