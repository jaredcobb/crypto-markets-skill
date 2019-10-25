from mycroft import MycroftSkill, intent_file_handler
import requests
import json

class CryptoMarkets(MycroftSkill):
    def __init__(self):
        self.log.info('Initializing Crypto Markets Skill...')
        self.url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
        MycroftSkill.__init__(self)

    @intent_file_handler('price.crypto.intent')
    def handle_price_crypto(self, message):
        coin = message.data.get('coin')
        if coin is not None:
            self.log.info('Identified the coin request. Calling the CoinGecko API for ' + str(coin))
            apiResponse = requests.get(self.url)
            if apiResponse.ok:
                apiData = json.loads(apiResponse.content)
                self.speak_dialog('price.crypto', {'coin': coin})
            else:
                self.speak_dialog('missing.crypto')
        else:
            self.speak_dialog('missing.crypto')

def create_skill():
    return CryptoMarkets()
