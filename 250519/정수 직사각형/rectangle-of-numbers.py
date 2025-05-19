n,m = list(map(int,input().split()))

matrix = []
for _ in range(n):
    matrix.append([0]*m)

val = 1
for i in range(n):
    for j in range(m):
        matrix[i][j] = val
        val += 1

for i in range(n):
    print(' '.join(map(str,matrix[i])))