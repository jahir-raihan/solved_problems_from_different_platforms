for _ in range(int(input())):
    n, k = map(int, input().split())

    a = sorted(list(map(int, input().split())))

    res = 0
    for i in a:
        if i > 0:
            res += i
        elif k > 0 and i < 0:
            res += i * -1
            k -= 1

    print(res)
