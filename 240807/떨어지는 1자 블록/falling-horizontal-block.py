n, m, k = tuple(map(int,input().split()))
matrix = [list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def get_height():
    for i in range(n):
        for j in range(m):
            if matrix[i][k-1+j] != 0:
                height = i-1
                return height

height = get_height()

for i in range(k-1,m+1):
    matrix[height][i] = 1

for matrix_ in matrix:
    print(' '.join(map(str,matrix_)))