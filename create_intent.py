from google.cloud import dialogflow
import os
import json
from typing import List
from dotenv import load_dotenv


def create_intent(project_id: str, display_name: str, training_phrases: List[str], message_texts: List[str]) -> str:
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
    return response.display_name


def main():
    load_dotenv()
    project_id = os.environ['DIALOGFLOW_PROJECT_ID']
    with open('job_questions.json', 'r', encoding='utf-8') as f:
        intent_data = json.load(f)
    
    try:
        create_intent(project_id, intent_data['intent_name'], intent_data['training_phrases'], [intent_data['response']])
    except Exception as e:
        print(f"Ошибка при создании интента: {e}")
        raise


if __name__ == '__main__':
    main()