import sys
sys.setrecursionlimit(10000)
n, m = map(int, input().split())
res = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0,1,0,-1], [1,0,-1,0]

def count_safe(limit):
    visited = [[False] * m for _ in range(n)]
    count = 0

    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return
        if visited[x][y] or res[x][y] <= limit:
            return
        visited[x][y] = True
        for dx, dy in zip(dxs,dys):
            new_x, new_y = x + dx, y + dy
            dfs(new_x, new_y)

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and res[i][j] > limit:
                dfs(i,j)
                count += 1
    return count

max_val = 0
k = 0

for i in range(1, 101):
    safe = count_safe(i)
    if safe >= max_val:
        max_val = safe
        k = i

print(k, max_val)