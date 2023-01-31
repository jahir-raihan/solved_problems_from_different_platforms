# cook your dish here
for _ in range(int(input())):
    n, w = map(int, input().split())

    a = sorted(list(map(int, input().split())))
    res = 0
    cnt = 0
    for i in range(n - 1, -1, -1):
        if res >= w:
            break
        else:
            res += a[i]
            cnt += 1
    print(n - cnt)

