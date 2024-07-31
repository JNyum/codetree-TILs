# n, k = tuple(map(int,input().split()))
# buckets = {}
# for _ in range(n):
#     candy, number = tuple(map(int,input().split()))
#     buckets[number] = candy


# res = []
# for i in range(k,100-k):
#     count = 0
#     for j in range(1,k+1):
#         try:
#             count += buckets[i+j]
#         except: pass
#         try:
#             count += buckets[i-j]
#         except: pass
#     res.append(count)
#     count = 0
# print(max(res))

n, k = tuple(map(int, input().split()))
buckets = {}
for _ in range(n):
    candy, number = tuple(map(int, input().split()))
    buckets[number] = candy

max_candies = 0

# Iterate over all possible basket numbers
for i in range(1, 101):
    current_candies = 0
    # Check all baskets within k range
    for j in range(-k, k + 1):
        if i + j in buckets:
            current_candies += buckets[i + j]
    # Update maximum candies found
    if current_candies > max_candies:
        max_candies = current_candies

print(max_candies)