import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from google.cloud import dialogflow
from google.protobuf.json_format import MessageToDict
from dotenv import load_dotenv
import os

load_dotenv()


vk_session = vk_api.VkApi(token=os.getenv('VK_GROUP_TOKEN'))
vk_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
language_code = 'ru-RU'


def detect_intent_text(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(request={"session": session, "query_input": query_input})
    return MessageToDict(response._pb)

def handle_message(event, vk_api):
    session_id = str(event.user_id)
    response = detect_intent_text(project_id, session_id, event.text, language_code)
    if not response['queryResult']['intent'].get('is_fallback', False):
        vk_api.messages.send(
            user_id=event.user_id,
            message=response['queryResult']['fulfillmentText'],
            random_id=random.randint(1, 1000)
        )

if __name__ == "__main__":
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            handle_message(event, vk_api)