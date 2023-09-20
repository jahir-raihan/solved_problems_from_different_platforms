t = int(input())

for _ in range(t):

    n, h = map(int, input().split())

    a = [int(i) for i in input().split()]
    s = sum(a)
    a.sort()

    if s < h:
        print(0)
    else:

        res = 0
        for i in a:
            if s - i < h:
                res = i
                break
            s -= i
        print(res)