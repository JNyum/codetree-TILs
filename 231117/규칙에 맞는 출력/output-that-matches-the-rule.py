n = int(input())

for h in range(n+1, 0, -1):
    for w in range(h, n+1):
        print(w, end=' ')
    if h == n+1:
        continue
    print()