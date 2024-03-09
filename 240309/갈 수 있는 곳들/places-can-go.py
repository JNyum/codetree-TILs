from collections import deque
n, k = tuple(map(int,input().split()))
res = [list(map(int,input().split())) for _ in range(n)]
dots = [tuple(map(int,input().split())) for _ in range(k)]
# 오 아 왼 위
dxs, dys = [0,1,0,-1], [1,0,-1,0]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dq = deque()
res_count = 0

for dot in dots:
    x, y = dot[0] - 1, dot[1] - 1
    if res[x][y] == 0:
        res_count += 1
        dq.append((x, y))
        res[x][y] = 1

while dq:
    x, y = dq.popleft()
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if in_range(new_x, new_y) and res[new_x][new_y] == 0:
            res_count += 1
            dq.append((new_x, new_y))
            res[new_x][new_y] = 1
print(res_count)