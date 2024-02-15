def summary(*arg):
    return sum(arg)


def subtract(*arg):
    for i in range(len(arg)):
        if i == 0:
            sub = arg[i]
        else:
            sub -= arg[i]
    return sub


def multiply(*arg):
    for i in range(len(arg)):
        if i == 0:
            mult = arg[i]
        else:
            mult *= arg[i]
    return mult


def divide(*arg):
    for i in range(len(arg)):
        if i == 0:
            mult = arg[i]
        else:
            mult /= arg[i]
    return mult