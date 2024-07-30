n = int(input())
# N E S W
directions = ['N','E','S','W']
dir_x = [0,1,0,-1]
dir_y = [1,0,-1,0]
res_x, res_y = 0,0
for i in range(n):
    direction, x = input().split()
    x = int(x)
    for i in range(x):
        res_x += dir_x[directions.index(direction)]
        res_y += dir_y[directions.index(direction)]
print(res_x,res_y)