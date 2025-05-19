n, m = tuple(map(int,input().split()))

matrix1 = [list(map(int,input().split())) for _ in range(n)]
matrix2 = [list(map(int,input().split())) for _ in range(n)]

res = []
for i in range(n):
    tmp = []
    for j in range(m):
        if matrix1[i][j] == matrix2[i][j]:
            tmp.append(0)
        else:
            tmp.append(1)
    res.append(tmp)

for i in range(n):
    print(' '.join(map(str,res[i])))