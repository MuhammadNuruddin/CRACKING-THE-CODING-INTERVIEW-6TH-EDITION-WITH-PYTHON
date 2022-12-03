def matrix_flip(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)//2
    m = n - 1
    for i in range(n):
        for j in range(n):
            top = matrix[i][i] #upper left

            matrix[i][i] = matrix[m - i][j] # upper left -> lower left

            matrix[m - i][j] = matrix[m - i][m - j] # lower left -> lower right

            matrix[m - i][m - j] = matrix[i][m - j] # lower right -> upper right

            matrix[i][m - j] = top # upper right -> upper left
    return True

matrix = [[20,3,9,17],[1,3,4,5],[2,10,23,10],[2,32,10,1]]
matrix_flip(matrix)
print(matrix)