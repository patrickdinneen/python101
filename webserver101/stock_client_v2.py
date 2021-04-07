import requests
import time
from pprint import pprint


def get_price(stonk_code):
    response = requests.get(f'http://localhost:5000/price/{stonk_code}')
    if response:
        return response.json()
    else: 
        print(f'Error! sleeping and retrying')
        time.sleep(1)
        return get_price(stonk_code)


if __name__ == '__main__':
    stonk_codes = ['GME', 'TSLA']

    for i in range(20):
        for code in stonk_codes:
            price = get_price(code)
            print(f'Iteration {i}')
            print(f'Stonk {code}')
            pprint(price)

            time.sleep(0.2)

    print('DONE!')
    time.sleep(15)

    stonk_codes = ['GME', 'TSLA', 'MSFT']

    for i in range(20):
        for code in stonk_codes:
            price = get_price(code)
            print(f'Iteration {i}')
            print(f'Stonk {code}')
            pprint(price)

            time.sleep(0.2)