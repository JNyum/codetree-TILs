matrix = []
for _ in range(4):
    matrix.append(list(map(int,input().split())))

res = 0
for i in range(4):
    for j in range(i+1):
        res += matrix[i][j]
print(res)