n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
# 1. 중복 확인 함수
duplicate = []
def is_it_duplicated(num):
    if num in duplicate:
        return True
    else:
        duplicate.append(num)
        return False

# 2. 반복문
max_val = -1
for num in nums:
    if num >= max_val:
        if is_it_duplicated(num):
            max_val = -1
        else:
            max_val = num
print(max_val)