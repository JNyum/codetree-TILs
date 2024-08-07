n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
x,y = map(lambda x:x-1,tuple(list(map(int,input().split()))))

bomb_range = matrix[x][y]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

matrix[x][y] = 0
for i in range(bomb_range):
    for j in range(bomb_range):
        if in_range(x+i,y):
            matrix[x+i][y] = 0
        if in_range(x, y+j):
            matrix[x][y+j] = 0
        if in_range(x-i,y):
            matrix[x-i][y] = 0
        if in_range(x, y-j):
            matrix[x][y-j] = 0
a = 0
while a < n:
    for i in range(n-1,0,-1):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][j] = matrix[i-1][j]
                matrix[i-1][j] = 0
    a += 1
for matrix_ in matrix:
    print(' '.join(map(str,matrix_)))