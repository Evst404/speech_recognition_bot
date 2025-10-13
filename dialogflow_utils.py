from google.cloud import dialogflow
from google.protobuf.json_format import MessageToDict
from typing import Dict


def detect_intent_text(project_id: str, session_id: str, text: str, language_code: str) -> Dict:
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(request={"session": session, "query_input": query_input})
    return MessageToDict(response._pb)