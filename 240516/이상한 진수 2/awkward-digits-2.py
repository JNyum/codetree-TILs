n = input()
if n == '1':
    print(0)
else:
    num = []
    for i in range(len(n)):
        num.append(n[i])
    index = 0
    while index < len(n):
        if num[index] == '0':
            num[index] = '1'
            break
        index += 1
    print(int(''.join(num),2))