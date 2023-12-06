n = int(input())
res = [list(map(int,input().split())) for _ in range(n)]
max_val = 0
def count_coins(h,w):
    coins = res[h][w:w+3].count(1) + res[h+1][w:w+3].count(1) + res[h+2][w:w+3].count(1)
    return coins

for h in range(0,n-3+1):
    for w in range(0,n-3+1):
        max_val = max(max_val, count_coins(h,w))
        if max_val == 7:
            break
print(max_val)