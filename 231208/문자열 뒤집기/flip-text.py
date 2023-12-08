n = input()

to_zero = 0
to_one = 0

for i in range(len(n)-1):
    if n[i] != n[i+1] and n[i] == '1':
        to_zero += 1
    if n[i] != n[i+1] and n[i] == '0':
        to_one += 1
if n[-1] == '0':
    to_one += 1
else:
    to_zero += 1
print(min(to_one, to_zero))