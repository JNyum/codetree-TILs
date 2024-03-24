n = int(input())
res = [list(map(int,input().split())) for _ in range(n)]
max_val = 0
for i in range(n):
    for j in range(n-2):
        val = res[i][j] + res[i][j+1] + res[i][j+2]
        max_val = max(max_val, val)
print(max_val)