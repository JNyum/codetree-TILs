from pprint import pprint
n, m = tuple(map(int,input().split()))
res = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b = tuple(map(int,input().split()))
    res[a-1][b-1] = res[b-1][a-1] = 1
count = 0
visited = [False]*n

def dfs(start):
    global count
    visited[start] = True
    for i in range(n):
        if res[start][i] == 1 and not visited[i]:
            # visited[i] == True
            count += 1
            dfs(i)




dfs(1)
print(count)