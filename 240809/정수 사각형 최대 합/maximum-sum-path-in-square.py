n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
res_matrix = [[0]*n for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

res_matrix[0] = matrix[0]

for i in range(1,n):
    for j in range(n):
        if in_range(i,j):
            res_matrix[i][j] = max(res_matrix[i][j-1] + matrix[i][j], res_matrix[i-1][j] + matrix[i][j])

print(res_matrix[n-1][n-1])