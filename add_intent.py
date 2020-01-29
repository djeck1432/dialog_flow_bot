import json
from dialogflow_v2 import IntentsClient


def create_intent(new_intent):
    client = IntentsClient()
    parent = client.project_agent_path('massive-sandbox-266519')
    for phrase in new_intent:
        intent = {
            'display_name': phrase,
            'messages': [{
                "text":
                    {"text": [new_intent[phrase]["answer"]]}
            }], 'training_phrases': [
                {
                    "parts": [{"text": phrase}]
                } for phrase in new_intent[phrase]["questions"]

            ]}
        response = client.create_intent(parent, intent)


def main():
    with open('file.json', 'r') as training_phrases:
        new_intent = json.load(training_phrases)
    create_intent(new_intent)


if __name__ == '__main__':
    main()
