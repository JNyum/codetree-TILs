matrix1 = [list(map(int,input().split())) for _ in range(3)]
input()
matrix2 = [list(map(int,input().split())) for _ in range(3)]


res = []
for i in range(3):
    tmp = []
    for j in range(3):
        tmp.append(matrix1[i][j] * matrix2[i][j])
    res.append(tmp)

for i in range(3):
    print(' '.join(map(str,res[i])))