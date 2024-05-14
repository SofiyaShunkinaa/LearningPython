from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import time


def main():
    while True:
        print("Введите текст:")
        text = input()

        if text.isdigit() and int(text) == 0:
            break

        start_time = time.time()
        encrypted = encrypt(text)
        end_time = time.time()
        print(f"Зашифрованный текст: {encrypted} | {end_time - start_time} sec")

        start_time = time.time()
        decrypted = decrypt(encrypted)
        end_time = time.time()
        print(f"Расшифрованный текст: {decrypted.decode()} | {end_time - start_time} sec")

        input("Нажмите Enter для продолжения...")


def encrypt(text):
    key = b'\xea\xee\xe2\xe0\xeb\xe5\xe2\xe0'
    iv = b'\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8'
    cipher = DES.new(key, DES.MODE_CFB, iv)
    padded_text = pad(text.encode(), DES.block_size)
    encrypted = cipher.encrypt(padded_text)
    return encrypted


def decrypt(text):
    key = b'\xea\xee\xe2\xe0\xeb\xe5\xe2\xe0'
    iv = b'\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8'
    cipher = DES.new(key, DES.MODE_CFB, iv)
    decrypted = cipher.decrypt(text)
    unpadded_text = unpad(decrypted, DES.block_size)
    return unpadded_text


if __name__ == "__main__":
    main()
