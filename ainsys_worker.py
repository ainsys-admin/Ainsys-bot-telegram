import requests

from database.db_api import get_fields, get_webhook, get_entity_name


def add_new_entity(entity_id):
    headers = {
        'Content-Type': 'application/json',
    }
    webhook_url = get_webhook(entity_id)
    data = {
        "entity": {
            "id": int(entity_id),
            "name": get_entity_name(entity_id).upper()
        },
        "action": "CREATE",
        "payload": get_fields(entity_id)
    }

    print(webhook_url)
    print(data)

    response = requests.post(webhook_url, headers=headers, json=data)
    response.raise_for_status()
    print(response.text)

    return True
