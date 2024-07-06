matrix = [list(map(int,input().split())) for _ in range(19)]

def in_range(x,y):
    return 0<=x<19 and 0<=y<19

def row_win(x,y,num):
    for i in range(5):
        if in_range(x,y+i) and matrix[x][y+i] != num:
            return False
    return True

def col_win(x,y,num):
    for i in range(5):
        if in_range(x+i,y) and matrix[x+i][y] != num:
            return False
    return True


# def win(x,y,num):
#     if row_win(i,j,num):
#         print(num)
#         print(i+1,j+3)
#         return
#     if col_win(i,j,num):
#         print(num)
#         print(i+3,j+1)
#         return
def win():
    for i in range(19):
        for j in range(19):
            if matrix[i][j] != 0:
                num = matrix[i][j]
                if row_win(i,j,num):
                    print(num)
                    print(i+1,j+3)
                    return
                if col_win(i,j,num):
                    print(num)
                    print(i+3,j+1)
                    return
    print(0)
    return
win()