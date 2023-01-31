for i in range(int(input())):
    a, b, c, d, k = map(int, input().split())

    cal = abs(c - a) + abs(d - b)
    if cal == k or ((cal - k) % 2 == 0 and cal < k):
        print('YES')
    else:
        print('NO')