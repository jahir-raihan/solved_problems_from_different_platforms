t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    idx = [0]*(n+1)
    for index, val in enumerate(arr):
        idx[val] = index + 1
    res = []
    if idx[n] > max(idx[1], idx[2]):
        res = [idx[n], max(idx[1], idx[2])]
    elif idx[n] < min(idx[1], idx[2]):
        res = [idx[n], min(idx[1], idx[2])]
    else:
        res = [idx[1], idx[2]]
    print(*res)