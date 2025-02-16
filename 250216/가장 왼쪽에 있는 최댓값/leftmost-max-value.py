n = int(input())
nums = list(map(int,input().split()))


idxes = []
while True:
    max_val = 0
    idx = 0
    for i in range(len(nums)):
        if nums[i] > max_val:
            max_val = nums[i]
            idx = i
    idxes.append(idx+1)
    if idx == 0:
        break
    
    nums = nums[:idx]
print(' '.join(map(str,idxes)))