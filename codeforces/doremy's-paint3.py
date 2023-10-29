from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    a = map(int, input().split())

    freq = Counter(a)
    if len(freq) > 2:
        print('NO')
    else:
        is_equal = True
        prev = None
        if n % 2 == 0:
            for v in freq.values():
                if prev is not None and v != prev:
                    is_equal = False
                else:
                    prev = v
        else:
            for v in freq.values():
                if prev is not None and abs(v - prev) > 1:
                    is_equal = False
                else:
                    prev = v
        print('YES' if is_equal else 'NO')

