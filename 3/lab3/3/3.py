list = [3, 5, 8, 1, 2, 9, -5, -1]
count = 0
for i in range(len(list)):
    for j in range(i, len(list)):
        if list[i] == -list[j]:
            count = count + 1
print(count)


