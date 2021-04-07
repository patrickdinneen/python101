from flask import Flask
from datetime import datetime
import stonks
app = Flask(__name__)

@app.route('/price/<stonk_code>', methods=['GET'])
def price(stonk_code):
    stonk = stonks.all_stonks.get(stonk_code.lower())

    if stonk:
        return {
            'stonk_code': stonk.code,
            'price': stonk.get_price(),
            'timestamp': datetime.utcnow()
        }
    else:
        return f'No such stonk: {stonk_code}', 404
