n, m = tuple(map(int,input().split()))
res = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b = tuple(map(int,input().split()))
    res[a-1][b-1] = res[b-1][a-1] = 1

visited = [False]*n
count = 0


def dfs(v):
    global count

    for curr_v in range(0, n):
        if res[v][curr_v] and not visited[curr_v]:
            visited[curr_v] = True
            count += 1
            dfs(curr_v)

# for res_ in res:
#     print(res_)

visited[0] = True
dfs(0)
print(count)

# n, m = tuple(map(int,input().split()))
# res = [[0]*(n+1) for _ in range(n+1)]
# for _ in range(m):
#     a,b = tuple(map(int,input().split()))
#     res[a][b] = res[b][a] = 1

# visited = [False]*n
# count = 0


# def dfs(v):
#     global count

#     for curr_v in range(1, n+1):
#         if res[v][curr_v] and not visited[curr_v]:
#             visited[curr_v] = True
#             count += 1
#             dfs(curr_v)

# for res_ in res:
#     print(res_)

# visited[1] = True
# dfs(1)
# print(count)