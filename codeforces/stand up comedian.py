for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a == 0:
        if b > 0 or c > 0 or d > 0:
            print(1)
        else:
            print(0)
    else:
        if b > c:
            b, c = c, b
        res = a + (2 * min(b, c))
        c -= b
        res += min(a + 1, c + d)
        print(res)