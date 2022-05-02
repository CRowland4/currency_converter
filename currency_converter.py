import requests


class Converter:
    def __init__(self):
        self.owned = ''
        self.wants = ''
        self.amount = 0
        self.cache = {'usd': 0, 'eur': 0}
        self.conversions = ''

    def get_initial_info(self):
        """Gets the currency to be converted and adds the relevant USD and EUR rates to the cache."""
        self.owned = input()
        self.conversions = requests.get(f'http://www.floatrates.com/daily/{self.owned}.json').json()
        if self.owned != 'usd':
            self.cache['usd'] = self.conversions['usd']['rate']
        if self.owned != 'eur':
            self.cache['eur'] = self.conversions['eur']['rate']
        return

    def main_loop(self):
        """The main function of the converter. Call this to run the script."""
        while True:
            self._get_new_info()
            if not self.wants:
                break
            self._cash_out()

        return

    def _get_new_info(self):
        """Gets the desired currency from the user and the amount of owned currency they want to convert.""""
        self.wants = input()
        if not self.wants:
            return
        self.amount = int(input())
        return

    def _check_cache(self):
        """Checks to see if the necessary exchange rate is already in the cache."""
        print("Checking the cache...")
        if self.wants in self.cache.keys():
            return True
        else:
            return False

    def _cash_out(self):
        """Gives the amount of the desired curreny after conversion, and adds the rate to the cache if it wasn't already there."""
        if self._check_cache():
            print("Oh! It is in the cache!")
            received = self.amount * self.cache[self.wants]
            print(f'You received {received} {self.wants}.')
            return
        else:
            print("Sorry, but it is not in the cache!")
            self.cache[self.wants] = self.conversions[self.wants]['rate']
            received = self.cache[self.wants] * self.amount
            print(f'You received {received} {self.wants}.')
            return


atm = Converter()
atm.get_initial_info()
atm.main_loop()
