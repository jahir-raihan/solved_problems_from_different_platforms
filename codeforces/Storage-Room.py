t = int(input())

for _ in range(t):
    n = int(input())
    arr = [2 ** 30 - 1 for _ in range(n)]
    mat = [0 for _ in range(n)]

    for i in range(n):
        vals = [int(v) for v in input().split()]
        mat[i] = vals
        for j in range(n):
            if i != j:
                arr[i] &= mat[i][j]
                arr[j] &= mat[i][j]
    ok = True

    for i in range(n):
        for j in range(n):
            if i != j and ((arr[i] | arr[j]) != mat[i][j]):
                ok = False

    if not ok:
        print("NO")
    else:
        print("YES")
        print(*arr)