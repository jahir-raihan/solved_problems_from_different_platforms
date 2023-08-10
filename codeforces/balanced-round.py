t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    a.sort()
    res = 0
    cur_count = 0
    i, j = 0, 1
    while j < n:
        if a[j] - a[i] > m:
            res = max(cur_count, res)
            i = j
            j = i + 1
            cur_count = 0
        else:
            cur_count += 1
            i += 1
            j += 1
    res = max(cur_count, res) + 1
    print(n - res)
