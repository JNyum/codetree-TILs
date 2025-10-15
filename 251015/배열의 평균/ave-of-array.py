matrix = []
for _ in range(2):
    nums = list(map(int,input().split()))
    matrix.append(nums)

# 가로
for i in range(2):
    print(round(sum(matrix[i]) / 4,1), end=' ')
print()

# 세로
for j in range(4):
    res = 0
    for i in range(2):
        res += matrix[i][j]
    print(round(res/2,1),end=' ')
print()

total_sum = sum(matrix[0]) + sum(matrix[1])
print(round(total_sum/8,1))