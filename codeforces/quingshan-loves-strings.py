t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    s = input()
    t = input()
    res = 'YES'

    t_valid = True
    for i in range(1, m):
        if t[i-1] == t[i]:
            t_valid = False
            break

    s_valid = True
    for i in range(1, n):
        if s[i-1] == s[i]:
            s_valid = False
            break
    if (t_valid and s_valid) or s_valid:
        pass
    elif not t_valid and not s_valid:
        res = 'NO'
    else:
        for i in range(1, n):
            if s[i-1] == s[i] and (t[0] == s[i-1] or t[-1] == s[i]):
                res = 'NO'
                break
    print(res)
