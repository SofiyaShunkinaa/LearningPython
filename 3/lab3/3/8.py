matrix = [
    [1, 3, 3, 8],
    [4, 5, 6, 7],
    [7, 9, 10, 1]
]

for i in range(len(matrix)):
    min = 1
    max = 1
    min_j = 0
    max_j = 0
    for j in range(len(matrix[0])):
        if matrix[i][j] < min:
            min = matrix[i][j]
            min_j = j
        if matrix[i][j] > max:
            max = matrix[i][j]
            max_j = j
    matrix[i][min_j], matrix[i][max_j] = matrix[i][max_j], matrix[i][min_j]
print(matrix)

