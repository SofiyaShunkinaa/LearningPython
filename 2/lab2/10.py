number = input('Enter a number from 1 to 999: ')
index = len(number)
lastNum = int(number[index-1])

if lastNum == 1:
    print(number, " рубль")
if 2 <= lastNum <= 4:
    print(number, "рубля")
if 5 <= lastNum <= 9 or lastNum == 0:
    print(number, "рублей")
