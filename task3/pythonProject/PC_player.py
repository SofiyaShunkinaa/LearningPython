from random import random
from SKey import SKey
from HMAC import Hmac


class PC_player:
    def __init__(self, paramCount):
        self.key = None
        self.hmac = None
        self.paramCount = paramCount

    def make_choice(self):
        return random.randint(self.paramCount)

    def get_key(self):
        self.key = SKey(32)
        self.key.generate_secrete_key()
        return self.key

    def get_hmac(self, choice_message):
        self.hmac = Hmac(self.key, choice_message)
        self.hmac.generate_hmac()



