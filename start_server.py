from flask import Flask, request, abort

from ainsys_worker import add_new_entity

app = Flask(import_name=__name__)


@app.route("/webhook", methods=['GET', 'POST'])
async def get_data():
    if request.method == 'POST':
        json = request.json

        if json['action'] == 'get_webhook':
            webhook = 'http://127.0.0.1:5000/webhook'
            return webhook

        if json['action'] == 'add_entity':
            response = add_new_entity(json['entity_id'])
            if response:
                print(json['entity_id'])
                return 'Cущность создана'


if __name__ == '__main__':
    app.run()
