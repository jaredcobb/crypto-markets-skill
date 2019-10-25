from mycroft import MycroftSkill, intent_file_handler
import requests
import json

class CryptoMarkets(MycroftSkill):
    def __init__(self):
        self.url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
        MycroftSkill.__init__(self)

    def initialize(self):
        self.register_entity_file("coin.entity")

    @intent_file_handler('price.crypto.intent')
    def handle_price_crypto(self, message):
        coin = message.data.get('coin')
        utterance = message.data.get('utterance')

        if coin is not None:
            self.log.info('Identified the coin request. Calling the CoinGecko API for ' + str(coin))
            coin = self.handle_synonyms(coin)

            response = requests.get(self.url)
            if response.ok:
                self.log.info('API Response was OK...')
                data = response.json()
                match = False

                for item in data:

                    if item['id'] == coin or item['symbol'] == coin or item['name'] == coin:
                        match = True
                        self.log.info('Matched a coin object: ' + str(item['name']))
                        self.speak_dialog('price.crypto', {'coin': item['name'], 'price': item['current_price']})

                if match == False:
                    self.speak_dialog('missing.crypto')

            else:
                self.log.info('API Response Failed...')
                self.speak_dialog('missing.crypto')
        else:
            self.log.info('Could not determine the requested coin...')
            self.speak_dialog('missing.crypto')

    def handle_synonyms(self, coin):
        synonyms = {
            "lightcoin": "litecoin",
            "light": "litecoin",
            "etherum": "ethereum",
            "ether": "ethereum"
        }

        if coin in synonyms:
            return synonyms[coin]
        else:
            return coin

def create_skill():
    return CryptoMarkets()
