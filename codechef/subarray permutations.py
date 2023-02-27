for _ in range(int(input())):
    n, k = map(int, input().split())
    tmp_k = k
    if k < 2 and n > k:
        print(-1)
    else:
        shift_number = None
        res = []
        for i in range(1, n+1):
            if i == tmp_k and shift_number is None:
                shift_number = i
            else:
                k -= 1
                res.append(i)
        res.append(shift_number)
        print(*res)

