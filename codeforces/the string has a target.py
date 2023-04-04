for _ in range(int(input())):
    n = int(input())
    s = [c for c in input()]
    min_s = min(s)
    idx = 0
    for i in range(n):
        if s[i] == min_s:
            idx = i
    s.pop(idx)
    print(min_s + ''.join(s))

