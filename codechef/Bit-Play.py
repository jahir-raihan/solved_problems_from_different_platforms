t = int(input())
MOD = 10 ** 9 + 7
for _ in range(t):
    n = int(input())
    s = input()

    res = 1

    for i in range(0, n - 2, 2):
        cur = 0
        a, b, c = int(s[i]), int(s[i + 1]), int(s[i + 2])

        if a | b == c:
            cur += 1
        if a ^ b == c:
            cur += 1
        if a & b == c:
            cur += 1

        res *= cur
        res %= MOD
    print(res)