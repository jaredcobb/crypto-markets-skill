from mycroft import MycroftSkill, intent_file_handler

class CryptoMarkets(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('price.crypto.intent')
    def handle_price_crypto(self, message):
        coin = message.data.get('coin')
        if coin is not None:
            self.speak_dialog('price.crypto', {'coin': coin})
        else:
            self.speak_dialog('missing.crypto')

def create_skill():
    return CryptoMarkets()
