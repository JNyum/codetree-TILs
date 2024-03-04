n, m = tuple(map(int,input().split()))
res = [list(map(int,input().split())) for _ in range(n)]
# 오, 아
dxs, dys = [0,1], [1,0]
visited = [[False]*m for _ in range(n)]
can = 0

def in_range(x,y):
    return x >= 0 and x <= n-1 and y >= 0 and y <= m-1

def dfs(now_x, now_y):
    global can
    visited[now_x][now_y] = True
    if now_x == n-1 and now_y == m-1:
        can = 1
    for dx, dy in zip(dxs, dys):
        new_x, new_y = now_x + dx, now_y + dy
        if in_range(new_x,new_y) and not visited[new_x][new_y] and res[new_x][new_y] == 1:
            dfs(new_x,new_y)
        
dfs(0,0)
print(can)
# n, m = map(int, input().split())
# res = [list(map(int, input().split())) for _ in range(n)]
# # 오, 아
# dxs, dys = [0, 1], [1, 0]
# visited = [[False] * m for _ in range(n)]
# can = 0

# def dfs(now_x, now_y):
#     global can
#     visited[now_x][now_y] = True
#     if now_x == n - 1 and now_y == m - 1:
#         can = 1
#         return
#     for dx, dy in zip(dxs, dys):
#         new_x, new_y = now_x + dx, now_y + dy
#         if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y] and res[new_x][new_y] == 1:
#             dfs(new_x, new_y)

# dfs(0, 0)
# print(can)