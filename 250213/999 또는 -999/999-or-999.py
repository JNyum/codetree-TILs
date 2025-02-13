def max_val(nums):
    res = -1000
    for num in nums:
        if num == 999 or num == -999:
            break
        elif num > res:
            res = num
    return res

def min_val(nums):
    res = 1000
    for num in nums:
        if num == 999 or num == -999:
            break
        elif num < res:
            res = num
    return res

nums = list(map(int,input().split()))
print(max_val(nums), min_val(nums))