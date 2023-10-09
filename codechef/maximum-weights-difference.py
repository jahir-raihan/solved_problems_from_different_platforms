t = int(input())

for _ in range(t):

    n, k = map(int, input().split())

    a = [int(i) for i in input().split()]

    a.sort()
    n_k = n - k
    if n_k > k:
        a_sum = sum(a[:k])
        b_sum = sum(a[k:])
    else:
        a_sum = sum(a[:n_k])
        b_sum = sum(a[n_k:])

    print(b_sum - a_sum)
