x1, y1, x2, y2 = map(lambda x:x+1000, tuple(map(int,input().split())))
xx1, yy1, xx2, yy2 = map(lambda x:x+1000, tuple(map(int,input().split())))

res = [[0]*2001 for _ in range(2002)]

for i in range(x1,x2+1):
    for j in range(y1,y2+1):
        res[i][j] = 1
for i in range(xx1,xx2+1):
    for j in range(yy1,yy2+1):
        res[i][j] = 0
min_x, min_y, max_x, max_y = 2001,2001,0,0
for i in range(x1,x2+1):
    for j in range(y1,y2+1):
        if res[i][j] == 1:
            min_x = min(min_x,i)
            min_y = min(min_y,j)
            max_x = max(max_x,i)
            max_y = max(max_y,j)
# print(max_x, min_x, max_y, min_y)
print((max_x-min_x)*(max_y-min_y) if (min_x,min_y,max_x,max_y) != (2001,2001,0,0) else 0)