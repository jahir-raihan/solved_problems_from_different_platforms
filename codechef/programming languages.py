for i in range(int(input())):
    a, b, a1, b1, a2, b2 = map(int, input().split())

    x1 = sorted([a, b])
    if sorted([a1, b1]) == x1:
        print(1)
    elif sorted([a2, b2]) == x1:
        print(2)
    else:
        print(0)
