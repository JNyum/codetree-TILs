a, b = tuple(map(int,input().split()))

def is_num(n):
    res = []
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            res.append(i) 
            if (i**2) != n: 
                res.append(n // i)
        
    if sum(res) == 2*n:
        return True
    else:
        return False
count = 0
for num in range(a,b+1):
    if is_num(num):
        count += 1
    else:
        continue
print(count)