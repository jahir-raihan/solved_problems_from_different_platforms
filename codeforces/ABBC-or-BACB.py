t = int(input())

for _ in range(t):
    s = input()
    res = 0
    if s[0] == 'B' or s[-1] == 'B' or 'BB' in s:
        res = s.count('A')
    else:
        split_s = s.split('B')
        total_len = 0
        min_len = 1e15
        for i in split_s:
            total_len += len(i)
            min_len = min(min_len, len(i))
        res = total_len - min_len

    print(res)


