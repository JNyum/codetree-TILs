n, q = tuple(map(int,input().split()))
nums = list(map(int,input().split()))
for i in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        print(nums[query[1]-1])
    elif query[0] == 2:
        if query[1] in nums:
            print(nums.index(query[1])+1)
        else:
            print(0)
    else:
        res = nums[query[1]-1:query[2]]
        print(' '.join(map(str,res)))