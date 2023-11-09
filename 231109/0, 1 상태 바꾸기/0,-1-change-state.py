n, m = tuple(map(int,input().split()))
res = list(map(int,input().split()))

for i in range(m):
    a, b, c = tuple(map(int,input().split()))
    if a == 1:
        res[b-1] = c
    elif a == 2:
        for j in range(b-1,c):
            res[j] = abs(res[j]-1)
    elif a == 3:
        res[b-1:c] = 0
    else:
        res[b-1:c] = 1
print(' '.join(map(str,res)))