n = int(input())
res = [list(map(int,input().split())) for _ in range(n)]

def square(x,y):
    count = 0
    for i in range(3):
        for j in range(3):
            if res[x+i][y+j] == 1:
                count += 1
    return count

max_val = 0
for i in range(n-2):
    for j in range(n-2):
        max_val = max(max_val, square(i,j))
print(max_val)