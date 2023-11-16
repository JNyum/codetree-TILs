n = int(input())
for h in range(n):
    for w in range(n):
        if h == 0 or (w % 2 != 0 and w >= h):
            print('* ', end='')
        else:
            print('  ', end='')
    print()