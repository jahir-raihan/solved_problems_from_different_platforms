for _ in range(int(input())):
    n, m = map(int, input().split())
    lst = input().split()
    res = [-1] * n
    added = {}
    cnt = 0
    pointer = n - 1
    for i in lst:
        if pointer == -1:
            break
        try:
            tmp = added[i]
            cnt += 1
        except:
            added[i] = 0
            cnt += 1
            res[pointer] = cnt
            pointer -= 1
    print(*res)
