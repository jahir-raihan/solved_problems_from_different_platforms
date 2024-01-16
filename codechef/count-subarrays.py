t = int(input())

for _ in range(t):
    n = int(input())

    a = [int(i) for i in input().split()]
    res = [1] * n
    for i in range(1, n):
        if a[i - 1] <= a[i]:
            res[i] = res[i - 1] + 1
    print(sum(res))