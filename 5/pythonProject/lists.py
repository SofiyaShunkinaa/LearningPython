import random

def randomList(n):
    return [random.randint(-99, 99) for _ in range(n)]


def randomMatrix(n):
    return [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]


def maxLength(X):
    for i in range(len(X)):
        if i == 0:
            index = i
            maxLength = len(X[i])
        else:
            if len(X[i]) > maxLength:
                maxLength = len(X[i])
                index = i
    return X[index]


def currentSums(X):
    new_list = []
    for i in range(len(X)):
        if i == 0:
            new_list.append(X[i])
        else:
            new_list.append(X[i]+new_list[i-1])
    return new_list


def threeSimbol(S):
    new_list = []
    n = int(len(S)/3)
    ostatok = len(S)%3
    start = 0
    for i in range(n):
        item = ''
        for j in range(start, start+3):
            item += S[j]
        start = j+1
        new_list.append(item)
    if ostatok != 0:
        item = ''
        for i in range(len(S)-ostatok, len(S)):
            item += S[i]
        new_list.append(item)
    return new_list
