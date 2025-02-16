n = int(input())
price = list(map(int, input().split()))

res = 0
# Write your code here!
for i in range(n):
    max_val = 0
    for j in range(i,n):
        if price[j] - price[i] > max_val:
            max_val = price[j] - price[i]
    if max_val > res:
        res = max_val
print(res)