n, m = tuple(map(int,input().split()))
res = [list(map(int,input().split())) for _ in range(n)]
# 오 아 왼 위
dxs, dys = [0,1,0,-1], [1,0,-1,0]
# visited = [[False]*m for _ in range(n)]

def half(ll):
    zero_sum = 0
    for i in range(n):
        zero_sum += ll[i].count(0)
    return zero_sum <= n*m // 2

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def dfs(x,y):
    visited[x][y] = True
    for dx, dy in zip(dxs,dys):
        new_x, new_y = x+dx, y+dy
        if in_range(new_x,new_y) and not visited[new_x][new_y]and res[new_x][new_y] > limit:
            dfs(new_x,new_y)
count = 0
limit = 1
res_count = []
while half(res):
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if res[i][j] <= limit:
                res[i][j] = 0
            if res[i][j] > limit and not visited[i][j]:
                dfs(i,j)
                count += 1
    res_count.append(count)
    limit += 1
    count = 0
max_value = max(res_count)
index = res_count.index(max_value) + 1
print(index, max_value)
# 여기서 dfs가 지나간 구역이 아니라 dfs가 실행된 횟수를 구해야된다.
# count가 어디 들어갈지 잘 생각해보자