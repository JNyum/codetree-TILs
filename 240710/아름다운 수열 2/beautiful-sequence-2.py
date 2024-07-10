from itertools import permutations

n, m = tuple(map(int,input().split()))
seq = list(map(int,input().split()))
sub = list(map(int,input().split()))

count = 0

if n >= m:
    target = list(permutations(sub,m))
    for i in range(n-m+1):
        if tuple(seq[i:i+m]) in target:
            count += 1
else:
    pass
print(count)