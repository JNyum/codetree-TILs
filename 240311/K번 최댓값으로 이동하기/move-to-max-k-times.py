from collections import deque
n, k = tuple(map(int,input().split()))
res = [list(map(int,input().split())) for _ in range(n)]
start = tuple(map(lambda x:x-1,tuple(map(int,input().split()))))
dxs, dys = [0,1,0,-1], [1,0,-1,0]

def in_range(x,y):
    return 0<=x<n and 0<=y<n
def min_matrix(value):
    for i in range(n):
        for j in range(n):
            if res[i][j] == value and visited[i][j]:
                return (i,j)

def bfs(s_x,s_y,s_v):
    visited = [[False]*n for _ in range(n)]
    dq = deque()
    dq.append((s_x,s_y))
    max_val = set()
    while dq:
        x,y = dq.popleft()
        visited[x][y] = True
        for dx,dy in zip(dxs,dys):
            new_x, new_y = x+dx, y+dy
            if in_range(new_x,new_y) and not visited[new_x][new_y] and res[new_x][new_y] < s_v:
                new_val = res[new_x][new_y]
                dq.append((new_x,new_y))
                max_val.add(new_val)
    if len(max_val) != 0:
        max_val = max(max_val)
        for i in range(n):
            for j in range(n):
                if res[i][j] == max_val and visited[i][j]:
                    return (i,j)
    else:
        return (x,y)
x, y = start[0], start[1]

for i in range(k):
    x, y = bfs(x,y,res[x][y])
print(x+1,y+1)