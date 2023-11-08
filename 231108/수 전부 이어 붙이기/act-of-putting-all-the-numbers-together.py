n = int(input())
count = 0
res = input().split()

for nums in res:
    for i in range(len(nums)):
        print(nums[i], end='')
        count += 1
        if count == 5:
            count = 0
            print()