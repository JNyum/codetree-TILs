nums = list(map(int,input().split()))

res_sum = nums[1]+nums[3]+nums[5]+nums[7]+nums[9]

res_avg = round((nums[2]+nums[5]+nums[8]) / 3, 1)

print(res_sum, res_avg)