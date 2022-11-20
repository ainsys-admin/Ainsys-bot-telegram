import requests

from database.db_api import get_fields_for_ainsys, get_webhook, get_entity_name


def update_data_ainsys(entity_id):
    headers = {
        'Content-Type': 'application/json',
    }
    webhook_url = get_webhook(entity_id)
    data = {
        "entity": {
            "id": int(entity_id),
            "name": get_entity_name(entity_id).upper()
        },
        "action": "UPDATE",
        "payload": ''
    }

    response = requests.post(webhook_url, headers=headers, json=data)
    response.raise_for_status()

    return True


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
        "payload": get_fields_for_ainsys(entity_id)
    }

    response = requests.post(webhook_url, headers=headers, json=data)
    response.raise_for_status()

    return True
