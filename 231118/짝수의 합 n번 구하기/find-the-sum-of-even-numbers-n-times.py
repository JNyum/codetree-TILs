n = int(input())

for i in range(n):
    a, b = tuple(map(int,input().split()))
    res = 0
    for num in range(a, b+1):
        if num % 2 == 0:
            res += num
    print(res)