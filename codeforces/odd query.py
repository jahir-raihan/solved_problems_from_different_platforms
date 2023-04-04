import sys
input = sys.stdin
for _ in range(int(input.readline())):
    n, q = map(int, input.readline().split())
    arr = list(map(int, input.readline().split()))
    a = [0] + arr
    for i in range(1, n+1):
        a[i] += a[i - 1]
    for j in range(q):
        l, r, k = map(int, input.readline().split())
        tmp_sum = (r-l+1) * k
        t_sum = a[r] - a[l-1]
        tmp = a[-1] - t_sum + tmp_sum
        print('YES' if tmp % 2 == 1 else 'NO')
