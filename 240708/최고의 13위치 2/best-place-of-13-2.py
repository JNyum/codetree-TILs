n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

def coins(x,y):
    count = 0
    for i in range(3):
        if matrix[x][y+i] == 1:
            count += 1
    return count

res = 0
for i in range(n):
    for j in range(n-2):
        for a in range(n):
            for b in range(n-2):
                if i == a and j <= b <= j+2:
                    continue
                else:
                    count = coins(i,j) + coins(a,b)
                    res = max(res,count)
print(res)