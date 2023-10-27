t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    h = [int(i) for i in input().split()]
    l = res = cur_sum = 0

    for r in range(n):
        if r > 0 and h[r - 1] % h[r] != 0:
            cur_sum = 0
            l = r
        cur_sum += a[r]
        while cur_sum > k:
            cur_sum -= a[l]
            l += 1
        res = max(res, r - l + 1)
    print(res)


