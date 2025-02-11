start, end = map(int, input().split())

def count_division(num):
    division = []
    for i in range(1, int(num**(1/2))+1):
        if num%i==0:
            division.append(i)
            if i < num//i:
                division.append(num//i)
    if len(division) == 3:
        return True
    else:
        return False
cnt = 0
for num in range(start,end+1):
    if count_division(num):
        cnt += 1
print(cnt)