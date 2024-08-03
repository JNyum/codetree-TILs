from collections import deque

characters = deque(input())

def encode(characters):
    n = len(characters)
    res = []
    res.append(characters[0])
    res.append(str(1))
    count = 1
    for i in range(1,n):
        if characters[i] == characters[i-1]:
            res[-1] = str(int(res[-1])+1)
        else:
            count = 1
            res.append(characters[i])
            res.append(str(1))
    res_string = ''.join(res)
    return len(res_string)

min_val = 100
n = len(characters)
while n >= 0:
    min_val = min(min_val, encode(characters))
    characters.appendleft(characters.pop())
    n -= 1
print(min_val)