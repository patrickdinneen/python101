import requests
import time
from pprint import pprint


def get_price(stonk_code):
    response = requests.get(f'http://localhost:5000/price/{stonk_code}')
    if response:
        return response.json()
    else:
        response.raise_for_status()


if __name__ == '__main__':
    stonk_codes = ['GME', 'TSLA']

    for i in range(20):
        for code in stonk_codes:
            price = get_price(code)
            print(f'Iteration {i}')
            print(f'Stonk {code}')
            pprint(price)

            time.sleep(0.2)