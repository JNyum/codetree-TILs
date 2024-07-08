nums = list(map(int,input().split()))

for i in range(len(nums)):
    if nums[i] == 0:
        print(nums[i-1]+nums[i-2]+nums[i-3])
        break