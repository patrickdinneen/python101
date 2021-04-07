from flask import Flask, abort
from datetime import datetime
import stonks
app = Flask(__name__)

@app.route('/price/<stonk_code>', methods=['GET'])
def price(stonk_code):
    now = datetime.utcnow()

    if now.second % 3 == 0:
        abort(502)


    stonk = stonks.all_stonks.get(stonk_code.lower())

    if stonk:
        return {
            'stonk_code': stonk.code,
            'price': stonk.get_price(),
            'timestamp': now
        }
    else:
        return 'No such stonk', 404
