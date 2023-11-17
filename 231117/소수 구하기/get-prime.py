import math
n = int(input())


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for num in range(2, n+1):
    if is_prime(num):
        print(num, end=' ')
    else:
        continue