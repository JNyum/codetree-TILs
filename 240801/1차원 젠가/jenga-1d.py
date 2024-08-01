n = int(input())
blocks = [int(input()) for _ in range(n)]
fir = tuple(map(int,input().split()))
first = [i for i in range(fir[0]-1,fir[1])]
sec = tuple(map(int,input().split()))
second = [i for i in range(sec[0]-1,sec[1])]

temp = []
for i in range(n):
    if i in first:
        continue
    else:
        temp.append(blocks[i])
blocks = temp
temp = []
for i in range(len(blocks)):
    if i in second:
        continue
    else:
        temp.append(blocks[i])
blocks = temp
print(len(blocks))
for i in blocks:
    print(i)