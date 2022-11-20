import json

import requests


def get_webhook(webhook_user, chat_id):
    headers = {
        "Content-Type": "application/json",
    }

    data = {
        'webhook': webhook_user,
        'chat_id': chat_id,
        'action': 'get_webhook'
    }
    webhook = requests.post("http://127.0.0.1:5000/webhook", data=json.dumps(data), headers=headers)

    return webhook


def add_entity_ainsys(user_id, entity_id, chat_id):
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        'action': 'add_entity',
        'user_id': user_id,
        'entity_id': entity_id,
        'chat_id': chat_id,
    }
    success_answer = requests.post("http://127.0.0.1:5000/webhook", data=json.dumps(data), headers=headers)
    return success_answer
