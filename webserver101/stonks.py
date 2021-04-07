from dataclasses import dataclass
import random


@dataclass
class Stonk:
    code: str
    price: float

    def get_price(self):
        self.price = self.price * (1 + random.randint(-100, 100)/5100)
        return self.price


all_stonks = {stonk.code.lower(): stonk for stonk in [Stonk('GME', 120.09),
                                                      Stonk('TSLA', 6000.88)]}
