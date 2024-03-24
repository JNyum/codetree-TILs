import sys
n = int(input())
nums = list(map(int,input().split()))
min_val = sys.maxsize
for i in range(n):
    res = 0
    for j in range(n):
        res += nums[j]*abs(i-j)
    min_val = min(min_val,res)
print(min_val)