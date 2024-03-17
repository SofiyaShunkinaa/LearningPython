# m=354 n=397 VARIANT=12
import math


print("--------Task 1------------------------------")
count = 0
for i in range(2, 397):
    flag = 0
    if i > 3:
        for j in range(2, i-1):
            if i % j == 0:
                flag += 1
        if flag == 0:
            count += 1
            print(i, end=" ")
    else:
        count += 1
        print(i, end=" ")
print()
print(f"Total count: {count}")
print(f"ln(n)/n: {397/math.log(397, math.e)}")
print()

print("--------Task 2------------------------------")
count = 0
for i in range(354, 397):
    flag = 0
    if i > 3:
        for j in range(2, i-1):
            if i % j == 0:
                flag += 1
        if flag == 0:
            count += 1
            print(i, end=" ")
    else:
        count += 1
        print(i, end=" ")
print()
print(f"Total count: {count}")