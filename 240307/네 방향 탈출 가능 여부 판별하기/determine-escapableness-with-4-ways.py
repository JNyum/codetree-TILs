from collections import deque
n, m = tuple(map(int,input().split()))
res = [list(map(int,input().split())) for _ in range(n)]
# 오 아 왼 위
dxs, dys = [0,1,0,-1], [1,0,-1,0]
visited = [[False]*m for _ in range(n)]
queue = deque()

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs():
    while queue:
        x,y = queue.popleft()
        if not in_range(x,y):
            continue
        if visited[x][y]:
            continue
        if res[x][y] != 1:
            continue

        visited[x][y] = True
        if x == n-1 and y == m-1:
            return 1
        for dx,dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            queue.append((new_x,new_y))
    return 0

queue.append((0,0))
# visited[0][0] = True
print(bfs())