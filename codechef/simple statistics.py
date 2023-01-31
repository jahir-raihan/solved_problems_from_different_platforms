for _ in range(int(input())):
    n, k = map(int, input().split())

    a = sorted(list(map(int, input().split())))
    l = sum(a[k: n - k]) / (n - 2 * k)
    print(l)
