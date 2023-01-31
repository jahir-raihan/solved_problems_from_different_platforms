for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    print(a[k] if k <= n - 1 else a[n - 1])