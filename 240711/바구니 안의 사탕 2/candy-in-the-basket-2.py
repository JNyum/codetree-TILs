n, k = tuple(map(int,input().split()))
buckets = {}
for _ in range(n):
    candy, number = tuple(map(int,input().split()))
    buckets[number] = candy
# print(buckets)

res = []
for i in range(k,100-k):
    count = 0
    for j in range(1,k+1):
        try:
            count += buckets[i+j]
        except: pass
        try:
            count += buckets[i-j]
        except: pass
    res.append(count)
    count = 0
print(max(res))