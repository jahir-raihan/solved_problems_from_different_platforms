for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    initial = a[0]
    for i in a:
        if i != initial:
            cnt += 1
    print(cnt)
