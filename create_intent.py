from google.cloud import dialogflow
from dotenv import load_dotenv
import os
import json


load_dotenv()

project_id = os.getenv('DIALOGFLOW_PROJECT_ID')


def create_intent(project_id, display_name, training_phrases, message_texts):
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases_parts = [{"parts": [{"text": phrase}]} for phrase in training_phrases]
    message = dialogflow.Intent.Message(text=dialogflow.Intent.Message.Text(text=message_texts))
    intent = dialogflow.Intent(
        display_name=display_name,
        training_phrases=training_phrases_parts,
        messages=[message]
    )
    response = intents_client.create_intent(request={"parent": parent, "intent": intent})
    print(f"Intent created: {response.display_name}")


if __name__ == '__main__':
    with open('job_questions.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    create_intent(project_id, data['intent_name'], data['training_phrases'], [data['response']])