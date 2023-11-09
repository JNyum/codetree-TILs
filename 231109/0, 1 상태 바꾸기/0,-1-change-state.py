n, m = map(int, input().split())
res = list(map(int, input().split()))
for _ in range(m) :
    a, b, c = map(int, input().split())
    if a == 1 :
        res[b-1] = c
    else :
        for i in range(b-1, c) :
            if a == 2 :
                res[i] = 1 - res[i]
            elif a == 3 :
                res[i] = 0
            else :
                res[i] = 1

print(*res)