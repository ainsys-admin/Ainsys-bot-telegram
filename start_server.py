from flask import Flask, request, abort

app = Flask(import_name=__name__)


@app.route("/webhook", methods=['GET', 'POST'])
async def get_data():
    if request.method == 'POST':
        json = request.json

        if json['action'] == 'get_webhook':
            webhook = 'http://127.0.0.1:5000/webhook'
            return webhook

        if json['action'] == 'add_entity':
            return 'сущность создана'
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
