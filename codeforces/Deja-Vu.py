t = int(input())

for _ in range(t):
    n, q = map(int, input().split())

    a = [int(i) for i in input().split()]
    x = set([int(i) for i in input().split()])

    for i in x:
        for idx, j in enumerate(a):
            if j % (2**i) == 0:
                a[idx] += 2**(i-1)
    print(*a)
