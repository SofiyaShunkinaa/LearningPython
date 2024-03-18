# m=354 n=397 VARIANT=12
import math


def getSimpleNums(n1, n2):
    count = 0
    for i in range(n1, n2):
        flag = 0
        if i > 3:
            for j in range(2, i - 1):
                if i % j == 0:
                    flag += 1
            if flag == 0:
                count += 1
                print(i, end=" ")
        else:
            count += 1
            print(i, end=" ")
    return count


def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors


def NOD(m, n):
    while n:
        m, n = n, m % n
    return m


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def concatenate_and_check_prime(m, n):
    concatenated_num = int(str(m) + str(n))
    return is_prime(concatenated_num)


print("--------Task 1------------------------------")
total = getSimpleNums(2, 397)
print()
print(f"Total count: {total}")
print(f"ln(n)/n: {397 / math.log(397, math.e)}")
print()

print("--------Task 2------------------------------")
total = getSimpleNums(354, 397)
print()
print(f"Total count: {total}")
print()

print("--------Task 3------------------------------")
product1 = prime_factors(354)
product2 = prime_factors(397)
product_str1 = ' * '.join(map(str, product1))
product_str2 = ' * '.join(map(str, product2))
print()
print(f"Product of prime factors 354 = {product_str1}")
print(f"Product of prime factors 397 = {product_str2}")
print()

print("--------Task 4------------------------------")
res = concatenate_and_check_prime(354, 397)
print()
print(f"Is number 354||397 prime?: {res}")
print()

print("--------Task 5------------------------------")
nod = NOD(354, 397)
print()
print(f"NOD of 354 and 397: {nod}")
print()

getSimpleNums(354, 397)