n, m = tuple(map(int,input().split()))
res = [[0]*m for _ in range(n)]
num = 1
for w in range(m):
    for h in range(n):
        res[h][w] = num
        num += 1
for res_ in res:
    print(' '.join(map(str,res_)))