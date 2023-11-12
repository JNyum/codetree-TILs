n = int(input())
char = 65
res = [['']*n for _ in range(n)]
x = 0
for w in range(n):
    for h in range(n):
        if w % 2 == 0:
            res[h][w] = chr(char+(x%26))
        else:
            res[(n-1)-h][w] = chr(char+(x%26))
        x += 1
for res_ in res:
    print(' '.join(map(str,res_)))