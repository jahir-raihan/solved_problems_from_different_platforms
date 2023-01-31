for i in range(int(input())):
    n, s = map(int, input().split())
    res = abs(n - abs(n - s))
    print(res)