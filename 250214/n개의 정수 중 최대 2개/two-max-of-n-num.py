n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
max_val = -(2**31)
second_max_val = -(2**31)+1
for num in nums:
    if num >= second_max_val and num < max_val:
        second_max_val = num
    elif num >= max_val:
        second_max_val = max_val
        max_val = num
        
print(max_val, second_max_val)
