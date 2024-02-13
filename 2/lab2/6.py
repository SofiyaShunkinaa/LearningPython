import random

a = random.randint(1,5)
b = int(input("Enter number between 1 and 5: "))
if a == b:
    print("Win! A: ", a, "B: ", b)
else:
    while a!=b:
        if a>b:
            print("Sorry your number is smaller")
        elif a<b:
            print("Sorry your number is bigger")
        b = int(input("Enter number again: "))
        if a == b:
            print("Win! A: ", a, "B: ", b)

