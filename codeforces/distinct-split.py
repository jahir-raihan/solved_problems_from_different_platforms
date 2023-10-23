import collections
t = int(input())


for _ in range(t):
    n = int(input())
    s = input()
    a = set(s[:1])

    b = collections.Counter(s[1:])
    cnt_b = len(b)

    max_val = 1
    i = 1
    while i < n:
        max_val = max(max_val, len(a) + cnt_b)
        a.add(s[i])

        b[s[i]] -= 1
        if b[s[i]] == 0:
            cnt_b -= 1
        i += 1
    print(max_val)
