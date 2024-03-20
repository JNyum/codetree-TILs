from collections import deque

n, t = tuple(map(int,input().split()))
dq1 = deque(list(map(int,input().split())))
dq2 = deque(list(map(int,input().split())))
dq3 = deque(list(map(int,input().split())))

while t:
    # v1 = dq1.pop()
    dq2.appendleft(dq1.pop())
    # v2 = dq2.pop()
    dq3.appendleft(dq2.pop())
    # v3 = dq3.pop()
    dq1.appendleft(dq3.pop())
    t -= 1
print(' '.join(map(str,dq1)))
print(' '.join(map(str,dq2)))
print(' '.join(map(str,dq3)))