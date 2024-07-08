from itertools import combinations

n, s = tuple(map(int,input().split()))
nums = list(map(int,input().split()))

indexes = combinations(nums,n-2)
sums = [abs(sum(index)-s) for index in indexes]
print(min(sums))