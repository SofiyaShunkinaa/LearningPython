def PerfectNumber(number):
    test_num = 0
    for i in range(1, int(number / 2) + 1):
        if number % i == 0:
            test_num += i
    if test_num == number:
        return True
    else:
        return False


print(PerfectNumber(6))
print(PerfectNumber(7))
