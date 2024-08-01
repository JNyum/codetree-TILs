from collections import deque

n, t = tuple(map(int,input().split()))
dq1 = deque(list(map(int,input().split())))
dq2 = deque(list(map(int,input().split())))


while t:
    temp1 = dq1.pop()
    temp2 = dq2.pop()
    dq1.appendleft(temp2)
    dq2.appendleft(temp1)
    t -= 1
print(' '.join(map(str,dq1)))
print(' '.join(map(str,dq2)))