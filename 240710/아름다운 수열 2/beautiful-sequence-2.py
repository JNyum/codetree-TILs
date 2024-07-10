from itertools import permutations

n, m = tuple(map(int,input().split()))
seq = list(map(int,input().split()))
sub = list(map(int,input().split()))

target = list(permutations(sub,m))

count = 0
for i in range(n-m+1):
    if tuple(seq[i:i+m]) in target:
        # print(tuple(seq[i:i+m]))
        count += 1
print(count)
# print(target)