n = int(input())
res = {}

for i in range(n):
    name, score = input().split()
    score = int(score)
    try:
        res[name] += score
    except:
        res[name] = score

if len(res) == 1:
    print(list(res.keys())[0])
else:
    value_set = sorted(set(res.values()))
    if len(value_set) == 1:
        print('Tie')
    else:
        res_key = [k for k, v in res.items() if v == value_set[1]]
        print(res_key[0])