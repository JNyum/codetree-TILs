n = int(input())
for h in range(n):
    for w in range(n):
        if h == 0 or w == (n-1) or h > w:
            print('* ', end='')
        else:
            print('  ', end='')
    print()