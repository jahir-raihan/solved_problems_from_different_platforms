t = int(input())

for _ in range(t):
    n = int(input())

    a = [int(i) for i in input().split()]

    b = [i for i in range(1, n+1)]

    if a[0] == 1:
        b[0] += 1

    for i in range(1, n):
        if a[i] == b[i-1] + 1:
            b[i] = b[i-1] + 2
        else:
            b[i] = b[i-1] + 1

    print(b[-1])


