n = int(input())

def sum_even(a,b):
    res = 0
    for num in range(a,b+1):
        if num % 2 == 0:
            res += num
    return res

for _ in range(n):
    a,b = list(map(int,input().split()))
    print(sum_even(a,b))