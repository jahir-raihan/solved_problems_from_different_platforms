t = int(input())

for _ in range(t):
    b, c, h = map(int, input().split())

    res = 3
    b -= 2
    c -= 1

    if b > c + h:
        res += c + h + (c + h)
    elif c + h > b:
        tmp = c + h

        res += b * 2
    else:
        res += b + c + h

    print(res)

