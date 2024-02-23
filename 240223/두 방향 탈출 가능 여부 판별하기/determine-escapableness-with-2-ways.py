n, m = tuple(map(int,input().split()))
res = [list(map(int,input().split())) for _ in range(n)]

visited = [[False]*n for _ in range(m)]

def can_go(x,y):
    return x >= 0 and x < n and y >= 0 and y < m and res[x-1][y-1] == 1

def dfs(x,y):
    dxs, dys= [1,0], [0,1]
    for dx, dy in zip(dxs,dys):
        next_x, next_y = x+dx, y+dy
        if can_go(next_x,next_y) and not visited[next_x][next_y]:
            visited[next_x][next_y] = True
            dfs(next_x,next_y)

visited[0][0] = True
dfs(0,0)
print(1 if visited[n-1][m-1] else 0)
# for res_ in res:
#     print(res_)