n, m = tuple(map(int,input().split()))
matrix = [list(input()) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def row_lee(x,y):
    res = 0
    if in_range(x,y+1) and in_range(x,y+2):
        if matrix[x][y+1] == 'E' and matrix[x][y+2] == 'E':
            res += 1
    if in_range(x,y-1) and in_range(x,y-2):
        if matrix[x][y-1] == 'E' and matrix[x][y-2] == 'E':
            res += 1
    return res

def col_lee(x,y):
    res = 0
    if in_range(x+1,y) and in_range(x+2,y):
        if matrix[x+1][y] == 'E' and matrix[x+2][y] == 'E':
            res += 1
    if in_range(x-1,y) and in_range(x-2,y):
        if matrix[x-1][y] == 'E' and matrix[x-2][y] == 'E':
            res += 1
    return res

def dia_lee(x,y):
    res = 0
    if in_range(x+1,y+1) and in_range(x+2,y+2):
        if matrix[x+1][y+1] == 'E' and matrix[x+2][y+2] == 'E':
            res += 1
    if in_range(x-1,y-1) and in_range(x-2,y-2):
        if matrix[x-1][y-1] == 'E' and matrix[x-2][y-2] == 'E':
            res += 1
    if in_range(x-1,y+1) and in_range(x-2,y+2):
        if matrix[x-1][y+1] == 'E' and matrix[x-2][y+2] == 'E':
            res += 1
    if in_range(x+1,y-1) and in_range(x+2,y-2):
        if matrix[x+1][y-1] == 'E' and matrix[x+2][y-2] == 'E':
            res += 1
    return res

count = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'L':
            count += row_lee(i,j) + col_lee(i,j) + dia_lee(i,j)

print(count)