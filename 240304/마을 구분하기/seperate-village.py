# from pprint import pprint
n = int(input())
res = [list(map(int,input().split())) for _ in range(n)]
count = 0
# pprint(res)
# 오 아 왼 위
dxs, dys = [0,1,0,-1], [1,0,-1,0]
visited = [[False]*n for _ in range(n)]


def in_range(x,y):
    return 0<=x<n and 0<=y<n
s = 1
ss = []

def dfs(x,y):
    global s
    visited[x][y] = True
    for dx, dy in zip(dxs,dys):
        new_x, new_y = x+dx, y+dy
        if in_range(new_x,new_y) and res[new_x][new_y] and not visited[new_x][new_y] == 1:
            s += 1
            dfs(new_x,new_y)
    return s

for i in range(n):
    for j in range(n):
        if res[i][j] == 1 and not visited[i][j]:
            ss.append(dfs(i,j))
            count += 1
            s = 1
print(count)
for i in sorted(ss):
    print(i)