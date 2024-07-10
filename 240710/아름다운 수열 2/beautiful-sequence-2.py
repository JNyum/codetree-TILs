# from itertools import permutations

# n, m = tuple(map(int,input().split()))
# seq = list(map(int,input().split()))
# sub = list(map(int,input().split()))

# count = 0

# if n >= m:
#     target = list(permutations(sub,m))
#     for i in range(n-m+1):
#         if tuple(seq[i:i+m]) in target:
#             count += 1
# else:
#     pass
# print(count)

from collections import Counter

n, m = tuple(map(int, input().split()))
seq = list(map(int, input().split()))
sub = list(map(int, input().split()))

count = 0

if n >= m:
    target_count = Counter(sub)
    window_count = Counter(seq[:m])
    
    if window_count == target_count:
        count += 1
    
    for i in range(1, n - m + 1):
        window_count[seq[i - 1]] -= 1
        if window_count[seq[i - 1]] == 0:
            del window_count[seq[i - 1]]
        
        window_count[seq[i + m - 1]] += 1
        
        if window_count == target_count:
            count += 1
else:
    pass

print(count)