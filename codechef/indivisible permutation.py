for _ in range(int(input())):
    n = int(input())
    if n > 2:
        res = [i for i in range(1, n + 1)]
        tmp = res.pop(1)
        res.append(tmp)
        print(*res)
    else:
        print(2, 1)
