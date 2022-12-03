matrix = [[11,2,4],[4,5,6],[10,8,-12]]
n = len(matrix)
m = n - 1
a,b = 0,0

for i in range(n):
    a+= matrix[i][i]
    b+= matrix[i][m - i]
print(abs(a-b))