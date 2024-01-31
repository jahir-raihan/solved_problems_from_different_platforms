t = int(input())

for _ in range(t):
    n, q = map(int, input().split())

    s = input()
    cur_max = -1
    i, j = 0, 0

    while j < n:
        if s[i] == s[j]:
            cur_max = max(cur_max, j - i + 1)
            j += 1
        else:
            i = j

    for _ in range(q):
        s += input()

    res = [cur_max]

    while j < n + q:
        if s[i] == s[j]:
            cur_max = max(cur_max, j - i + 1)
            j += 1
            res.append(cur_max)

        else:
            i = j
    print(*res)



