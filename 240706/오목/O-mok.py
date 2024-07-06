matrix = [list(map(int,input().split())) for _ in range(19)]

def in_range(x,y):
    return 0<=x<19 and 0<=y<19

def row_win(x,y,num):
    for i in range(5):
        if not in_range(x,y+i):
            return False
        if matrix[x][y+i] != num:
            return False
    return True

def col_win(x,y,num):
    for i in range(5):
        if not in_range(x+i,y):
            return False
        if matrix[x+i][y] != num:
            return False
    return True

def leftup_win(x,y,num):
    for i in range(5):
        if not in_range(x+i,y+i):
            return False
        if matrix[x+i][y+i] != num:
            return False
    return True

def leftdown_win(x,y,num):
    for i in range(5):
        if not in_range(x+i,y-i):
            return False
        if matrix[x+i][y-i] != num:
            return False
    return True





def win():
    for i in range(19):
        for j in range(19):
            if matrix[i][j] != 0:
                num = matrix[i][j]
                if row_win(i,j,num):
                    print(num)
                    print(i+1,j+3)
                    print(1)
                    return
                if col_win(i,j,num):
                    print(num)
                    print(i+3,j+1)
                    print(2)
                    return
                if leftup_win(i,j,num):
                    print(num)
                    print(i+3,j+3)
                    print(3)
                    return
                if leftdown_win(i,j,num):
                    print(num)
                    print(i+3,j-1)
                    print(4)
                    return
    print(0)
    return
win()