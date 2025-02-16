nums = list(map(int,input().split()))

over_val = 1001
under_val = 0

for num in nums:
    if num > 500 and num < over_val:
        over_val = num
    if num < 500 and num > under_val:
        under_val = num
print(under_val, over_val)