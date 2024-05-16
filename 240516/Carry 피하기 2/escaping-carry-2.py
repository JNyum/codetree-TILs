from itertools import combinations

n = int(input())
nums = [int(input()) for _ in range(n)]

coms = list(combinations(nums,3))
# print(coms)

def is_carry(a,b,c):
    while a or b or c:
        digit_a, digit_b, digit_c = a%10, b%10, c%10
        if digit_a + digit_b + digit_c >= 10:
            return False
        a //= 10
        b //= 10
        c //= 10
    return True
res = []

for a,b,c in coms:
    if is_carry(a,b,c):
       res.append(a+b+c) 

print(max(res) if res else -1)