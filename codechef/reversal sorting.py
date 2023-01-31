for _ in range(1):
    n, x = 5 , 7#map(int, input().split())

    a = [3, 2, 2, 3, 3]#[int(i) for i in input().split()]
    i, j = 0, 1
    res = True
    while j < n:
        if a[i] <= a[j]:
            i = j
            j = j + 1
        elif a[i] > a[j]:
            sm = a[i] + a[j]
            if sm <= x:
                j += 1
            else:
                res = False
                break
    print('YES' if res else 'NO')