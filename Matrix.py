def matrix_inversion(matrix):
    if not matrix:
        return
    n = len(matrix)
    n_m = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            n_m[j][n - i - 1] = matrix[i][j]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = n_m[i][j]

M = [[1,2,3],[4,5,6],[7,8,9]]
matrix_inversion(M)
for row in M:
    print(row)