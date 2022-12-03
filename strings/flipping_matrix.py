matrix = [[20,3,9,17],[1,3,4,5],[2,10,23,10],[2,32,10,1]]
n = len(matrix)//2
m = len(matrix) - 1
sum = 0
for i in range(n):
    for j in range(n):
        sum+= max(matrix[i][j],matrix[i][m-j],matrix[m-i][j],matrix[m-i][m-j])

print(sum)