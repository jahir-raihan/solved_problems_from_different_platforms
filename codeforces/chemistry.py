import collections
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    s = input()
    set_s = set(s)
    freq = collections.Counter(s)

    for c in set_s:
        fr = freq[c]
        if fr % 2 == 1 and k > 0:
            freq[c] -= 1
            k -= 1
        if k == 0:
            break

    odd_count = 0
    for c in set_s:
        if freq[c] % 2 == 1:
            odd_count += 1

    print('YES' if odd_count < 2 else 'NO')





