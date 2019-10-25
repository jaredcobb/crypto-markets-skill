from mycroft import MycroftSkill, intent_file_handler
import requests
import json

class CryptoMarkets(MycroftSkill):
    def __init__(self):
        self.url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
        MycroftSkill.__init__(self)

    @intent_file_handler('price.crypto.intent')
    def handle_price_crypto(self, message):
        coin = message.data.get('coin')
        if coin is not None:
            self.log.info('Identified the coin request. Calling the CoinGecko API for ' + str(coin))
            response = requests.get(self.url)
            if response.ok:
                self.log.info('API Response was OK...')
                data = response.json()

                for key, coinObject in data.items():
                    if coinObject.id == coin or coinObject.symbol == coin or coinObject.name == coin:
                        self.log.info('Matched a coin object: ' + str(coinObject.name))
                        price = coinObject.current_price
                        self.speak_dialog('price.crypto', {'coin': coinObject.name, 'price': price})
            else:
                self.log.info('API Response Failed...')
                self.speak_dialog('missing.crypto')
        else:
            self.log.info('Could not determine the requested coin...')
            self.speak_dialog('missing.crypto')

def create_skill():
    return CryptoMarkets()
