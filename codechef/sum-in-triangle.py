t = int(input())
# Yeah copied -> But trying to understand it hardly will do it at night.
for _ in range(t):
    n = int(input())

    lst = [[int(i) for i in input().split()] for j in range(n)]

    for j in range(n - 2, -1, -1):
        for k in range(0, j + 1):
            lst[j][k] += max(lst[j + 1][k], lst[j + 1][k + 1])
    print(lst[0][0])