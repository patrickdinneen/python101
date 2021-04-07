import requests
import time
from pprint import pprint


def get_price(stonk_code, retries_remaining=5):
    response = requests.get(f'http://localhost:5000/price/{stonk_code}')
    if response:
        return response.json()
    elif response.status_code >= 500 and retries_remaining > 0:
        print(f'Gateway down, sleeping and retrying')
        time.sleep(1)
        return get_price(stonk_code, retries_remaining=retries_remaining - 1)
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