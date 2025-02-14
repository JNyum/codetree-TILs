n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
max_val = -1
for num in nums:
    if num > max_val:
        max_val = num
    elif num == max_val:
        max_val = -1
print(max_val)