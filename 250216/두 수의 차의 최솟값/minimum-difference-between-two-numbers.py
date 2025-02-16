n = int(input())
nums = list(map(int,input().split()))


min_val = 1000
for i in range(n):
    for j in range(i+1,n):
        if abs(nums[i]-nums[j]) < min_val:
            min_val = abs(nums[i]-nums[j])
print(min_val)