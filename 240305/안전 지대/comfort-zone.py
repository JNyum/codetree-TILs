import sys
sys.setrecursionlimit(10**6)

n, m = tuple(map(int,input().split()))
res = [list(map(int,input().split())) for _ in range(n)]
# 오 아 왼 위
dxs, dys = [0,1,0,-1], [1,0,-1,0]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def dfs(x,y):
    visited[x][y] = True
    for dx, dy in zip(dxs,dys):
        new_x, new_y = x+dx, y+dy
        if in_range(new_x,new_y) and not visited[new_x][new_y] and res[new_x][new_y] > limit:
            dfs(new_x,new_y)
res_count = []
for limit in range(1,101):
    visited = [[False]*m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if res[i][j] <= limit:
                res[i][j] = 0
            if res[i][j] > limit and not visited[i][j]:
                dfs(i,j)
                count += 1
    res_count.append(count)
max_value = max(res_count)
index = res_count.index(max_value) + 1
print(index, max_value)