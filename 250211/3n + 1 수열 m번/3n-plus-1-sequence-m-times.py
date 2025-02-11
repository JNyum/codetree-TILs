n = int(input())


def get_cnt(num):
    cnt = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (num * 3) + 1
        cnt += 1
    return cnt

for _ in range(n):
    m = int(input())
    print(get_cnt(m))