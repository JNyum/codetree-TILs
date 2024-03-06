# import sys
# sys.setrecursionlimit(10000)
n = int(input())
res = [list(map(int,input().split())) for _ in range(n)]
# 오 아 왼 위
dxs, dys = [0,1,0,-1], [1,0,-1,0]
visited = [[False]*n for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def dfs(x,y,value):
    global count
    if not in_range(x,y):
        return
    if visited[x][y]:
        return
    if res[x][y] != value:
        return
    visited[x][y] = True
    count += 1
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy
        dfs(new_x,new_y,value)
blocks = 0
counts = []
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count = 0
            v = res[i][j]
            dfs(i,j,v)
            counts.append(count)
            blocks +=1
            
# print(counts)
print(sum(1 for x in counts if x >= 4), max(counts))
# print()