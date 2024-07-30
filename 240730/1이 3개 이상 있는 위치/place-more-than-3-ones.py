n = int(input())
res = [list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

dxs = [-1,0,1,0]
dys = [0,1,0,-1]
ans = 0
for h in range(n):
    for w in range(n):
        count = 0
        for dx, dy in zip(dxs, dys):
            if in_range(dx+h,dy+w) and res[dx+h][dy+w] == 1:
                count += 1
        if count >= 3:
            ans += 1
print(ans)