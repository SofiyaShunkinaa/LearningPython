import sys
import Errors


def check_identical(lst):
    for i in range(len(lst)):
        if lst.count(lst[i]) > 1:
            return False
    return True


def input_check(params):
    print(params)
    if len(params) % 2 == 0:
        Errors.err1()
        new_params = input("Введите параметры через пробел: ").split()
        input_check(new_params)
    elif len(params) < 3:
        Errors.err3()
        new_params = input("Введите параметры через пробел: ").split()
        input_check(new_params)
    elif check_identical(params) == 0:
        Errors.err2()
        new_params = input("Введите параметры через пробел: ").split()
        input_check(new_params)
    else:
        print("Принятые параметры:", params)


input_check(sys.argv[1:])
