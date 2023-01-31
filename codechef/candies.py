for _ in range(int(input())):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    cur_max = -1
    cur = 0
    pref = [0] * (m + 1)
    for i in a:
        pref[i] += 1
    for i in range(m + 1):
        pref[i] += pref[i - 1]

    for i in range(1, m + 1):
        val = 0
        for j in range(i, m + 1, i):
            val += j // i * (pref[m if m < i + j - 1 else i + j - 1] - pref[j - 1])

        if val * c[i - 1] > cur_max:
            cur_max = val * c[i - 1]

    print(cur_max)