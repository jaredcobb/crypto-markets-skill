from mycroft import MycroftSkill, intent_file_handler


class CryptoMarkets(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('markets.crypto.intent')
    def handle_markets_crypto(self, message):
        self.speak_dialog('markets.crypto')


def create_skill():
    return CryptoMarkets()

