n, m = tuple(map(int,input().split()))
res = [list(map(int,input().split())) for _ in range(n)]
res_val = 0

# 행 확인
for h in range(n):
    max_count_h = 1
    h_count = 1
    for w in range(0,n-1):
        # res[h][w] res[h][w+1] 비교
        if res[h][w] == res[h][w+1]:
            h_count += 1
    # m과 연속 동일 수의 갯수 확인
    max_count_h = max(max_count_h, h_count)
    if max_count_h >= m:
        # print(h,w)
        res_val += 1

# print('--')

# 열 확인
for w in range(n):
    w_count = 1
    max_count_w = 1
    for h in range(n-1):
        # res[h][w] res[h+1][w] 비교
        if res[h][w] == res[h+1][w]:
            w_count += 1
    # m과 연속 동일 수의 갯수 확인
    max_count_w = max(max_count_w, w_count)
    if max_count_w >= m:
        # print(h,w)
        res_val += 1

print(res_val)