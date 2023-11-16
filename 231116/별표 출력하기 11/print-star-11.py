n = int(input())
for h in range(2*n+1):
    for w in range(2*n+1):
        if h == 0 or w == 0 or h % 2 == 0 or w % 2 == 0:
            print('* ', end='')
        else:
            print('  ', end='')
    print()