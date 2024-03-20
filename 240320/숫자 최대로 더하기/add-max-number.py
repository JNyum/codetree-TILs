n = int(input())
nums = list(map(int,input().split()))
nums.sort()

while len(nums) != 1:    
    min_val = min(nums)
    max_val = max(nums)
    nums = nums[1:-1]
    nums.append(max_val + (min_val/2))
    nums.sort()

print(round(nums[0],1))