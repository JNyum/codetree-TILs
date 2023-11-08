n = int(input())
res = []
for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            res.append(i) 
            if ( (i**2) != n) : 
                res.append(n // i)

res.sort()
print(' '.join(map(str, res)))