nums = list(map(int,input().split()))

max_val = 0
for num in nums:
    if num > max_val:
        max_val = num
print(max_val)