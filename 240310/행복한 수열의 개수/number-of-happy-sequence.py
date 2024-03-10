# n, m = tuple(map(int,input().split()))
# res = [list(map(int,input().split())) for _ in range(n)]

# def happy_row(x,y):
#     count = 1
#     for j in range(1,n):
#         if res[x][j-1] == res[x][j]:
#             count += 1
#     if count >= m:
#         return True
#     else:
#         return False

# def happy_col(x,y):
#     count = 1
#     for j in range(1,n):
#         if res[j-1][y] == res[j][y]:
#             count += 1
#     if count >= m:
#         return True
#     else:
#         return False

# res_count = 0
# for i in range(n):
#     if happy_col(0,i):
#         res_count += 1
#     if happy_row(i,0):
#         res_count += 1

# print(res_count)


# def count_happy_sequences(grid, m):
#     n = len(grid)
#     happy_count = 0
    
#     # 각 행에 대해 확인
#     for row in grid:
#         count = 1
#         for i in range(1, n):
#             if row[i] == row[i-1]:
#                 count += 1
#                 if count >= m:
#                     happy_count += 1
#             else:
#                 count = 1
                
#     # 각 열에 대해 확인
#     for j in range(n):
#         count = 1
#         for i in range(1, n):
#             if grid[i][j] == grid[i-1][j]:
#                 count += 1
#                 if count >= m:
#                     happy_count += 1
#             else:
#                 count = 1
                
#     return happy_count

# # 입력 받기
# n, m = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(n)]

# # 행복한 수열의 개수 출력
# print(count_happy_sequences(grid, m))


n, m = tuple(map(int, input().split()))
res = [list(map(int, input().split())) for _ in range(n)]

def happy_row(x, y):
    count = 1
    for j in range(1, n):
        if res[x][j-1] == res[x][j]:
            count += 1
        else:
            count = 1
        if count >= m:
            return True
    return False

def happy_col(x, y):
    count = 1
    for i in range(1, n):
        if res[i-1][y] == res[i][y]:
            count += 1
        else:
            count = 1
        if count >= m:
            return True
    return False

res_count = 0
for i in range(n):
    if happy_col(0, i):
        res_count += 1
    if happy_row(i, 0):
        res_count += 1

print(res_count)