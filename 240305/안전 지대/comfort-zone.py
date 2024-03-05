import sys
sys.setrecursionlimit(10000)

n, m = tuple(map(int,input().split()))
res = [list(map(int,input().split())) for _ in range(n)]
# 오 아 왼 위
dxs, dys = [0,1,0,-1], [1,0,-1,0]

def in_range(x,y):
    pass



def count_safe(limit):
    count = 0
    visited = [[False]*m for _ in range(n)]
    def dfs(x,y):
        if x<0 or x>=n or y<0 or y>=m:
            return
        if visited[x][y] or res[x][y] <= limit:
            return
        visited[x][y] = True
        for dx, dy in zip(dxs,dys):
            new_x, new_y = x+dx, y+dy
            dfs(new_x,new_y)

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and res[i][j] > limit:
                dfs(i,j)
                count += 1
    return count
counts = []
for k in range(1,100):
    counts.append(count_safe(k))
max_val = max(counts)
max_k = counts.index(max_val)+1
print(max_k, max_val)