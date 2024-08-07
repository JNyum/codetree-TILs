from collections import deque
n, r, c = tuple(map(int,input().split()))
matrix = [list(map(int,input().split())) for _ in range(n)]
x,y = r-1,c-1
# 위 아 왼 오
dxs, dys = [-1,1,0,0],[0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

values = []
dq = deque()
max_value = 0
dq.append((x,y))
while dq:
    x,y = dq.popleft()
    value = matrix[x][y]
    values.append(value)
    for dx,dy in zip(dxs,dys):
        n_x, n_y = x+dx, y+dy
        if in_range(n_x,n_y) and matrix[n_x][n_y] > value:
            dq.append((n_x,n_y))
            break

print(' '.join(map(str,values)))