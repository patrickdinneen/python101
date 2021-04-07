from flask import Flask, abort, request
from datetime import datetime
import stonks
app = Flask(__name__)

@app.route('/price/<stonk_code>', methods=['GET'])
def price(stonk_code):
    abort(502)


@app.route('/query-test', methods=['GET'])
def do_something_fancy():
    print(request.args.get('id'))
    return 'thanks'