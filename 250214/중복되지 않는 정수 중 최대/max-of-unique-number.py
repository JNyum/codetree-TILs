n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
# 1. 중복 확인 함수
duplicate = []
not_duplicate = []

def is_it_duplicated(num):
    if num in duplicate:
        if num in not_duplicate:
            not_duplicate.pop(not_duplicate.index(num))
        return True
    else:
        duplicate.append(num)
        return False


for num in nums:
    if is_it_duplicated(num):
        continue
    else:
        duplicate.append(num)
        not_duplicate.append(num)

max_val = -1

if not_duplicate:
    for num in not_duplicate:
        if num > max_val:
            max_val = num
print(max_val)