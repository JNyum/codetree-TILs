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
        visited[x][y] = True
        if x == n-1 and y == m-1:
            return 1
        for dx,dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if in_range(new_x,new_y) and not visited[new_x][new_y] and res[new_x][new_y] == 1:
                queue.append((new_x,new_y))
    return 0

queue.append((0,0))
visited[0][0] = True
print(bfs())