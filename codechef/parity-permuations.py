t = int(input())
MOD = int(1e9 + 7)
for _ in range(t):
    n, k = map(int, input().split())
    a = map(int, input().split())

    fact = [1, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fact[i] = i * fact[i - 1]
        fact[i] %= MOD

    e = o = 0

    for i in a:
        e += i % 2 == 1
        o += i % 2 == 0

    if k == 0:
        if e == n or o == n:
            print(fact[n])
        else:
            print(0)

    else:
        if e > o:
            e, o = o, e

        if e == o:
            ans = 1
            ans *= fact[e]
            ans *= fact[o]
            ans *= 2
            ans %= MOD
            print(ans)
        elif e + 1 == o:
            ans = 1
            ans *= fact[e]
            ans *= fact[o]
            ans %= MOD
            print(ans)
        else:
            print(0)