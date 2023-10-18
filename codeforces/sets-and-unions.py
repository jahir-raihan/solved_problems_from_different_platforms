t = int(input())

for _ in range(t):
    n = int(input())
    sets = []
    for _ in range(n):
        sets.append(set(int(x) for x in input().split()[1:]))

    finalset = set()

    for s in sets: finalset |= s

    ret = 0

    for val in finalset:
        candset = set()
        for s in sets:
            if val in s: continue
            candset |= s
        ret = max(ret, len(candset))

    print(ret)
