n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
min_val = 2**31
cnt = 1
for num in nums:
    if min_val > num:
        min_val = num
        cnt = 1
    elif min_val == num:
        cnt += 1
    
print(min_val,cnt)