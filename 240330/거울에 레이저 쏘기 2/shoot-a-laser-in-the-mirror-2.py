from math import ceil
n = int(input())
res = [input() for _ in range(n)]
x = int(input())
direction_index = ceil(x/n)
# 1 2 3 4
dxs, dys = [1,0,-1,0], [0,-1,0,1]
def reflect(direction_index,mirror):
    if mirror == '/':
        if direction_index == 1:
            direction_index = 2
        if direction_index == 2:
            direction_index = 1
        if direction_index == 3:
            direction_index = 4
        if direction_index == 4:
            direction_index = 3
    if mirror == '\\':
        if direction_index == 1:
            direction_index = 4
        if direction_index == 2:
            direction_index = 3
        if direction_index == 3:
            direction_index = 2
        if direction_index == 4:
            direction_index = 1
    return direction_index
def start(x):
    range_x = [i for i in range(n)]
    range_y = [i for i in range(n)]
    if direction_index == 1:
        s_x, s_y = 0, range_y[x-1]
    if direction_index == 2:
        s_x, s_y = range_x[(x-1)%n], n-1
    if direction_index == 3:
        s_x, s_y = n-1, range_y[::-1][(x-1)%n]
    if direction_index == 4:
        s_x, s_y = range_x[::-1][(x-1)%n], 0
    return s_x, s_y
def in_range(x,y):
    return 0<=x<n and 0<=y<n
s_x, s_y = start(x)
count = 0
# print(tuple(zip(dxs,dys)))
while in_range(s_x,s_y):
    direction = list(zip(dxs,dys))[reflect(direction_index,res[s_x][s_y])-1]
    s_x += direction[0]
    s_y += direction[1]
    count += 1
print(count)