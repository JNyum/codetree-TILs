# n, m = map(int, input().split())
# res = [list(map(int, input().split())) for _ in range(n)]
# dxs, dys = [0,1,0,-1], [1,0,-1,0]

# def count_safe(limit):
#     visited = [[False] * m for _ in range(n)]
#     count = 0

#     def dfs(x, y):
#         if x < 0 or x >= n or y < 0 or y >= m:
#             return
#         if visited[x][y] or res[x][y] <= limit:
#             return
#         visited[x][y] = True
#         for dx, dy in zip(dxs,dys):
#             new_x, new_y = x + dx, y + dy
#             dfs(new_x, new_y)

#     for i in range(n):
#         for j in range(m):
#             if not visited[i][j] and res[i][j] > limit:
#                 dfs(i,j)
#                 count += 1
#     return count

# max_val = 0
# k = 0

# for i in range(1, 101):
#     safe = count_safe(i)
#     if safe >= max_val:
#         max_val = safe
#         k = i

# print(k, max_val)
N, M = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(N)]

def count_safe_areas(height_limit):
    visited = [[False] * M for _ in range(N)]
    safe_area_count = 0

    def dfs(x, y):
        if x < 0 or x >= N or y < 0 or y >= M:
            return
        if visited[x][y] or heights[x][y] <= height_limit:
            return
        visited[x][y] = True
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            dfs(new_x, new_y)

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and heights[i][j] > height_limit:
                dfs(i, j)
                safe_area_count += 1

    return safe_area_count

max_safe_areas = 0
best_K = 0

for K in range(1, 101):  # K의 범위는 1부터 100까지
    safe_areas = count_safe_areas(K)
    if safe_areas >= max_safe_areas:
        max_safe_areas = safe_areas
        best_K = K

print(best_K, max_safe_areas)