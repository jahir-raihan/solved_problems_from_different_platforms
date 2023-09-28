t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    lst = [1 for i in range(n // 2)] + [2 for i in range(n // 2)]
    s = (3 * n) // 2

    if s > k or (k - s) % 2 == 1 or k > (100000 * n) - (n / 2):
        lst = [-1]
    else:
        rem = k - s
        for i in range(n):
            lst[i] += min(99998, rem)
            rem -= min(99998, rem)

    print(*lst)
