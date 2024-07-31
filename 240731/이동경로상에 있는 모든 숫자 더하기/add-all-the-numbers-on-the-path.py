n, t = tuple(map(int,input().split()))
orders = list(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

x, y = n//2, n//2
# 오 아 왼 위
dxs,dys = [0,1,0,-1],[1,0,-1,0]
# dxdy = [(0,1),(1,0),(0,-1),(-1,0)]
direction = 3

res = matrix[x][y]
# print(matrix[x][y])
for order in orders:
    if order == 'F':
        if in_range(x+dxs[direction],y+dys[direction]):
            x,y = x+dxs[direction],y+dys[direction]
            res += matrix[x][y]
            # print(matrix[x][y])
    if order == 'R':
        direction = direction + 1
    if order == 'L':
        direction = direction - 1
    direction = (direction + 4) % 4
print(res)