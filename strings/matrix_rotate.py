"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

SOLUTION
Because we're rotating the matrix by 90 degrees, the easiest way to do this is to implement the rotation in
layers. We perform a circular rotation on each layer, moving the top edge to the right edge, the right edge
to the bottom edge, the bottom edge to the left edge, and the left edge to the top edge.


How do we perform this four-way edge swap? One option is to copy the top edge to an array, and then
move the left to the top, the bottom to the left, and so on. This requires O(N) memory, which is actually
unnecessary.
A better way to do this is to implement the swap index by index. In this case, we do the following:
1 - for i = 0 to n
2 - temp= top[i];
3 - top[i] = left[i]
4 - left[i] = bottom[i]
5 - bottom[i] = right[i]
6 - right[i] = temp

We perform such a swap on each layer, starting from the outermost layer and working our way inwards.
(Alternatively, we could start from the inner layer and work outwards.)
"""

def matrix_rotate(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    layer = 0
    while layer < (n//2):
        first = layer
        last = n - 1 - layer
        i = first
        while i < last:
            offset = i - first
            top = matrix[first][i] #top

            #left -> top
            matrix[first][i] = matrix[last - offset][first]

            #bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            #right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            #top -> right
            matrix[i][last] = top
            i+=1
        layer+=1
        # print(matrix)
    return True


def matrix_rotate_two(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]): return False
    n = len(matrix)
    m = n - 1
    for i in range(n//2):
        for j in range(i, m - i):    
            # top-left = matrix[i][j]
            # top-right = matrix[j][m - i]
            # bottom-left = matrix[m - j][i]
            # bottom-right = matrix[m - i][m - j]
            temp = matrix[i][j] #top
            #left -> top
            matrix[i][j] = matrix[m - j][i]
            #bottom -> left
            matrix[m - j][i] = matrix[m - i][m - j]
            #right -> bottom
            matrix[m - i][m - j] = matrix[j][m - i]
            #top -> right
            matrix[j][m - i] = temp
    return True


def print_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        print(matrix[i])

matrix = [[20,3,9,17],
          [1,3,4,5],
          [2,10,23,10],
          [2,32,10,1]]
print_matrix(matrix)
matrix_rotate_two(matrix)
print_matrix(matrix)
# print(matrix)
