from collections import deque
n, k = tuple(map(int,input().split()))
res = [list(map(int,input().split())) for _ in range(n)]
dots = [tuple(map(int,input().split())) for _ in range(k)]
# 오 아 왼 위
dxs, dys = [0,1,0,-1], [1,0,-1,0]
visited = [[False]*n for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dq = deque()
res_set = set()

def bfs():
    while dq:
        x, y = dq.popleft()
        visited[x][y] = True
        for dx, dy in zip(dxs,dys):
            new_x, new_y = x+dx, y+dy
            if in_range(new_x,new_y) and not visited[new_x][new_y] and res[new_x][new_y] == 0:
                dq.append((new_x,new_y))
                res_set.add((new_x,new_y))
                # print(res_set)

for dot in dots:
    x, y = dot[0]-1, dot[1]-1
    res_set.add((x,y))
    dq.append((x,y))
    bfs()
print(len(res_set))