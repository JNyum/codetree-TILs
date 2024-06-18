n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
    min_val = arr[i]
    for j in range(i,n):
        if min_val > arr[j]:
            temp = min_val
            min_val = arr[j]
            arr[j] = temp
    arr[i] = min_val
print(' '.join(map(str,arr)))