n, k, p, time = tuple(map(int,input().split()))
# 개발자 n명, 횟수 T번, 감염되면 K번 옮김, 처음 걸린 개발자 P번
# 개발자 : k

def is_infected(x):
    return res[x][0]
def can_infect(x):
    return True if res[x][1] > 0 else False

res = {}
for i in range(1,n+1):
    # res[i] = (감염여부, k)
    res[i] = [0,0]
res[p] = [1,k]
txy = [tuple(map(int,input().split())) for _ in range(time)]
txy.sort()

for t,x,y in txy:
    if is_infected(x) and is_infected(y):
        res[x][1] -= 1
        res[y][1] -= 1
    if not is_infected(x) and is_infected(y) and can_infect(y):
        res[x] = [1,k]
        res[y][1] -= 1
    if is_infected(x) and not is_infected(y) and can_infect(x):
        res[x][1] -= 1
        res[y] = [1,k]
    if not is_infected(x) and not is_infected(y):
        continue
for ress in res.values():
    print(ress[0], end='')