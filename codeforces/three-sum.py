t = int(input())

for _ in range(t):
    n = int(input())
    res = None

    br = False
    for i in range(1, n - 1):
        if i % 3 == 0:
            continue
        if br:
            break
        l = i + 1
        r = n - 2

        while l < r:
            if l % 3 == 0:
                l += 1
                continue
            if r % 3 == 0:
                r -= 1
                continue
            s = i + l + r
            if s > n:
                r -= 1
            elif s < n:
                l += 1
            else:
                res = [i, l, r]
                br = True
                break
    if br:
        print('YES')
        print(*res)
    else:
        print('NO')
