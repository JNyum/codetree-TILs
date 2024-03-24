string = input()
res = 0
for i in range(len(string)):
    if string[i] == '(':
        for j in range(i,len(string)):
            if string[j] == ')':
                res += 1
print(res)