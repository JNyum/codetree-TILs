matrix = []
for _ in range(2):
    nums = list(map(int,input().split()))
    matrix.append(nums)
res = 0
for i in range(2):
    res += sum(matrix[i])
    print(f"{sum(matrix[i])/4:.1f}",end=' ')
print()

for j in range(4):
    tmp = 0
    for i in range(2):
        tmp += matrix[i][j]
    print(f"{tmp/2:.1f}",end=' ')
print()
print(f"{res/8:.1f}")