matrix = [list(map(int,input().split())) for _ in range(19)]

def in_range(x,y):
    return 0<=x<19 and 0<=y<19

def row_win(x,y,color):
    for i in range(5):
        if matrix[x][y-2+i] != color:
            return False
    return True
def col_win(x,y,color):
    for i in range(5):
        if matrix[x-2+i][y] != color:
            return False
    return True
def leftup_win(x,y,color):
    for i in range(5):
        if matrix[x-2+i][y-2+i] != color:
            return False
    return True
def rightup_win(x,y,color):
    for i in range(5):
        if matrix[x+2-i][y-2+i] != color:
            return False
    return True

flag = False
for i in range(2,17):
    for j in range(2,17):
        if matrix[i][j] != 0:
            color = matrix[i][j]
            if row_win(i,j,color) or col_win(i,j,color) or leftup_win(i,j,color) or rightup_win(i,j,color):
                print(color)
                print(i+1,j+1)
                flag = True

if not flag:
    print(0)