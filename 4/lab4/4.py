def RemoveRowCol(K, L):
    matrix = [
        [0, 6, 8],
        [15, 5, 18],
        [0, 0, 0],
        [2, 1, 9],
    ]
    M = len(matrix)
    N = len(matrix[0])
    if K > M or L > N:
        return matrix
    else:
        for i in range(M):
            for j in range(N):
                if j < N and K < M and L < N and i < M:
                    if matrix[i][j] == K:
                        matrix.remove(matrix[i])
                    elif matrix[i][j] == L:
                        for k in range(M):
                            matrix[k].remove(matrix[k][j])
                    N = len(matrix[0])
                    M = len(matrix)
        return matrix


print(RemoveRowCol(0, 1))
print(RemoveRowCol(20, 1))
print(RemoveRowCol(2, 2))
