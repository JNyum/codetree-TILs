n, p = tuple(map(int,input().split()))
count = 0
res = []
num = n
while True:
    if count != 0 and res.count(num) == 2:
        break
    num = (num*n)%p
    res.append(num)
    # print(res)
    count += 1
print((count-1)-res.index(num))