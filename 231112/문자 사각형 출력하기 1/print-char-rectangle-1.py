n = int(input())
res = [['']*n for _ in range(n)]
char = 65
x = 0

for w in range(n-1, -1, -1):
    for h in range(n-1, -1, -1):
        res[h][w] = chr(char+(x%26))
        x += 1
for res_ in res:
    print(' '.join(res_))