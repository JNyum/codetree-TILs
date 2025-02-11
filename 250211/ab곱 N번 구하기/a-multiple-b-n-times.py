n = int(input())

for _ in range(n):
    a,b = list(map(int,input().split()))
    tmp = 1
    for i in range(a,b+1):
        tmp = tmp * i
    print(tmp)