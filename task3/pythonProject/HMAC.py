import hmac
import hashlib


class Hmac:
    def __init__(self, skey, message):
        self.skey = skey
        self.message = message

    def generate_hmac(self):
        return hmac.new(self.skey, self.message.encode(), hashlib.sha3_256).digest().hex()
