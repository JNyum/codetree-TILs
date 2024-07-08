nums = list(map(int,input().split()))
odd_sum = nums[0]+nums[2]+nums[4]+nums[6]+nums[8]
even_sum = nums[1]+nums[3]+nums[5]+nums[7]+nums[9]
print(abs(odd_sum-even_sum))