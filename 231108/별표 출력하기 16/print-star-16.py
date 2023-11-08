n = int(input())

for h in range(n, 0, -1):
    print(f'{" "*(n**2-h**2)}{"*"*h**2}')