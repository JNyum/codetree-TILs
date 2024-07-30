x = [0,1,0,-1]
y = [1,0,-1,0]

string = input()

index = 0

res_x, res_y = 0,0
for i in range(len(string)):
    if string[i] == 'L':
        index -= 1
    elif string[i] == 'R':
        index += 1
    else:
        res_x += x[index%4]
        res_y += y[index%4]
print(res_x, res_y)