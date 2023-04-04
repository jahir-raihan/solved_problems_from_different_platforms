for _ in range(int(input())):
    n = int(input())
    dic = {}
    s = input()
    res = True
    prev = None
    for c in s:
        if c == prev:
            continue
        elif c in dic:
            res = False
            break
        else:
            dic[c] = 1
        prev = c
    print('YES' if res else 'NO')