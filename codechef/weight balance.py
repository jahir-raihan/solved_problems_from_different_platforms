for i in range(int(input())):
    w1, w2, x1, x2, m = map(int, input().split())

    diff = w2 - w1
    min_possible = x1 * m
    max_possible = x2 * m

    if min_possible <= diff <= max_possible:
        print(1)
    else:
        print(0)
