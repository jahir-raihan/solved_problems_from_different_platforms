
for _ in range(int(input())):
    n = int(input())
    s = [c for c in input()]
    min_s = min(s)
    replaced = False
    res = ''
    for i in range(n):
        if (s[i] == min_s) and (i > 0) and (s[i - 1] != min_s) and (not replaced):
            replaced = True
            res = s[i] + res
        else:
            res += s[i]
    print(res)
