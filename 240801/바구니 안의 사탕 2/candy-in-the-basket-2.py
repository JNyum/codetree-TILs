n, k = tuple(map(int,input().split()))
buckets = [0]*100
for _ in range(n):
    candies, bucket = tuple(map(int,input().split()))
    buckets[bucket] += candies

max_value = 0

for i in range(k,100-k):
    value = sum(buckets[i-k:i+k+1])
    max_value = max(max_value,value)
print(max_value)