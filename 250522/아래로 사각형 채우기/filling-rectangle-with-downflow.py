n = int(input())

matrix = [[0]*n for _ in range(n)]
num = 1
for i in range(n):
    for j in range(n):
        matrix[j][i] = num
        num += 1
# print(matrix)
for i in range(n):
    print(' '.join(map(str,matrix[i])))