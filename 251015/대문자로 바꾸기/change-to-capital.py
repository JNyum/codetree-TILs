def up(char):
    return char.upper()
for _ in range(5):
    print(' '.join(map(up,input().split())))
    