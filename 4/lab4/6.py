def Fact(num):
    if num == 0:
        return 1
    else:
        rec = Fact(num-1)
        result = num*rec
        return result


def Fact2(num):
    if num == -1 or num == 0:
        return 1
    else:
        rec = Fact2(num-2)
        result = num*rec
        return result


print(Fact2(6))
print(Fact2(7))
