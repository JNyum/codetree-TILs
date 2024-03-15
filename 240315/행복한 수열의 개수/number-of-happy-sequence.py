n, m = tuple(map(int,input().split()))
res = [list(map(int,input().split())) for _ in range(n)]

def happy_row(x,y):
    count = 1
    for j in range(1,n):
        if res[x][j-1] == res[x][j]:
            count += 1
            if count >= m:
                # print('row',x,y)
                return True
        else:
            count = 1
    if count >= m:
        # print('row',x,y)
        return True
    return False

def happy_col(x,y):
    count = 1
    for j in range(1,n):
        if res[j-1][y] == res[j][y]:
            count += 1
            if count >= m:
                # print('col',x,y)
                return True
        else:
            count = 1
    if count >= m:
    #     print('col',x,y)
        return True
    return False

res_count = 0
for i in range(n):
    if happy_col(0,i):
        res_count += 1
    if happy_row(i,0):
        res_count += 1

print(res_count)


# n, m = tuple(map(int, input().split()))
# res = [list(map(int, input().split())) for _ in range(n)]

# def happy_row(x, y):
#     count = 1
#     for j in range(1, n):
#         if res[x][j-1] == res[x][j]:
#             count += 1
#         else:
#             count = 1
#         if count >= m:
#             return True
#     return False

# def happy_col(x, y):
#     count = 1
#     for i in range(1, n):
#         if res[i-1][y] == res[i][y]:
#             count += 1
#         else:
#             count = 1
#         if count >= m:
#             return True
#     return False

# res_count = 0
# for i in range(n):
#     if happy_col(0, i):
#         res_count += 1
#     if happy_row(i, 0):
#         res_count += 1

# print(res_count)





# n, m = tuple(map(int,input().split()))

# res = [list(map(int, input().split())) for _ in range(n)]

# def happy_row(x, y):
#     count = 1
#     if count >= m:
#         return True
#     for j in range(1, n):
#         if res[x][j-1] == res[x][j]:
#             count += 1
#             if count >= m:
#                 return True
#     # else:
#     #     count = 1
#     return False

# def happy_col(x, y):
#     count = 1
#     if count >= m:
#         return True
#     for i in range(1, n):
#         if res[i-1][y] == res[i][y]:
#             count += 1
#             if count >= m:
#                 return True
#     # else:
#     #     count = 1
#     return False

# res_count = 0
# for i in range(n):
#     if happy_row(i, 0):
#         res_count += 1
#     if happy_col(0, i):
#         res_count += 1

# print(res_count)