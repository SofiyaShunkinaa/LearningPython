matrix = [
    [1, 3, 3, 8],
    [4, 5, 6, 7],
    [7, 9, 10, 1]
]

for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        if matrix[j][i] % 2 == 0:
            flag = 1
    if flag == 0:
        print(i)
        first = 1
if first == 0:
    print(0)
