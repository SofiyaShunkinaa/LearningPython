import os


class SKey:
    def __init__(self, length):
        self.length = length

    def generate_secrete_key(self):
        key = os.urandom(self.length)
        return key