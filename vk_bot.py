import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dialogflow_utils import detect_intent_text
import os
from dotenv import load_dotenv


LANGUAGE_CODE = 'RU_RU'


def handle_message(event, vk_api_instance, project_id, language_code):
    session_id = f"vk-{event.user_id}"
    response = detect_intent_text(project_id, session_id, event.text, language_code)
    if not response['queryResult']['intent'].get('is_fallback', False):
        vk_api_instance.messages.send(
            peer_id=event.peer_id,
            message=response['queryResult']['fulfillmentText'],
            random_id=random.randint(1, 1000)
        )


def main():
    load_dotenv()
    vk_session = vk_api.VkApi(token=os.environ['VK_GROUP_TOKEN'])
    vk_api_instance = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    project_id = os.environ['DIALOGFLOW_PROJECT_ID']
    
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                handle_message(event, vk_api_instance, project_id, LANGUAGE_CODE)
    except Exception as e:
        print(f"Ошибка в работе VK бота: {e}")
        raise


if __name__ == '__main__':
    main()