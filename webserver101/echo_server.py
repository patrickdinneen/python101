import random

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/echo/<message>', methods=['GET'])
def echo(message):
    return message, 302

@app.route('/lucky', methods=['GET'])
def lucky():
    messages = ['hello', '¡Ola!', 'goodbye', 'Aloha']
    http_status = [200, 403, 502]

    result = {
        'message': random.choice(messages),
        'number': random.randint(0, 10)
    }

    return result, random.choice(http_status)
