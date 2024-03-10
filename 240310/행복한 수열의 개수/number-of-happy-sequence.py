n, m = tuple(map(int,input().split()))
res = [list(map(int,input().split())) for _ in range(n)]

def happy_row(x,y):
    count = 1
    for j in range(1,n):
        if res[x][j-1] == res[x][j]:
            count += 1
    # print('row',x,y,count)
    if count >= m:
        return True
    else:
        return False

def happy_col(x,y):
    count = 1
    for j in range(1,n):
        if res[j-1][y] == res[j][y]:
            count += 1
    # print('col',x,y,count)
    if count >= m:
        return True
    else:
        return False

res_count = 0
for i in range(n):
    if happy_col(0,i):
        # print('col',0,i)
        res_count += 1
    if happy_row(i,0):
        # print('row',i,0)
        res_count += 1

print(res_count)