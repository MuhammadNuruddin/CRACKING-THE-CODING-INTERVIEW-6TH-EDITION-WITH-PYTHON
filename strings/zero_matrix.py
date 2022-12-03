""""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.

SOLUTION
At first glance, this problem seems easy: just iterate through the matrix and every time we see a cell with
value zero, set its row and column to 0. There's one problem with that solution though: when we come
across other cells in that row or column, we'll see the zeros and change their row and column to zero. Pretty
soon, our entire matrix will be set to zeros.
One way around this is to keep a second matrix which flags the zero locations. We would then do a second
pass through the matrix to set the zeros.This would take O(MN) space.
Do we really need O(MN) space? No. Since we're going to set the entire row and column to zero, we don't
need to track that it was exactly cell [ 2] [ 4] (row 2, column 4). We only need to know that row 2 has a
zero somewhere, and column 4 has a zero somewhere.We'll set the entire row and column to zero anyway,
so why would we care to keep track of the exact location of the zero?
The code below implements this algorithm. We use two arrays to keep track of all the rows with zeros and all
the columns with zeros. We then nullify rows and columns based on the values in these arrays.
"""

def zero_matrix(matrix):
    row = [False] * len(matrix)
    column = [False] * len(matrix[0])

    # Store the row and column index with value 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = True
                column[j] = True

    # nullify rows
    for i in range(len(row)):
        if row[i]:
            nullify_row(matrix, i)

    # nullify column
    for j in range(len(column)):
        if column[j]:
            nullify_column(matrix, j)

    return matrix

def nullify_row(matrix,row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0


def nullify_column(matrix, column):
    for i in range(len(matrix)):
        matrix[i][column] = 0


def print_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        print(matrix[i])

matrix = [[20,3,9,17],
          [1,0,4,5],
          [2,10,23,0],
          [2,32,10,1]]

print_matrix(matrix)
zero_matrix(matrix)
print_matrix(matrix)