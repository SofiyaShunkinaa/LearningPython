import random
from SKey import SKey


class PC:
    def __init__(self, paramCount):
        self.key = None
        self.move = None
        self.paramCount = paramCount

    def make_choice(self):
        self.move = str(random.randint(1, self.paramCount))
        self.get_key()

    def get_key(self):
        key = SKey(32)
        self.key = key.generate_secrete_key()
        return self.key
