n = int(input())

nums = [i for i in range(1,n+1)]

def solution(n):
    is_prime = [True for x in range(n+1)]
    p = 2
    while (p * p < n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
    
    return prime_numbers

print(' '.join(map(str,solution(n))))