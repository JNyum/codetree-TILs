start, end = map(int, input().split())

def is_it_complete(num):
    divided = [1]
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            divided.append(i)
            if i < num//i:
                divided.append(num//i)
    if sum(divided) == num:
        return True
    else:
        return False
cnt = 0
for num in range(start,end+1):
    if is_it_complete(num):
        cnt+=1

print(cnt)