for _ in range(int(input())):
    s = list(input())
    n = len(s)

    lower = []
    upper = []

    for i in range(n):

        if s[i] == 'b':
            s[i] = ''
            if lower:
                s[lower.pop()] = ''
            continue

        if s[i] == 'B':
            s[i] = ''
            if upper:
                s[upper.pop()] = ''
            continue

        if 'a' <= s[i] <= 'z':
            lower += [i]
        else:
            upper += [i]
    print(''.join(s))

