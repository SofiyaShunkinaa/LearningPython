count = 0
start = 1
while start != 0:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        count = count+1
    start = num
print(count)