for _ in range(int(input())):
    n = int(input())
    s = input()
    res = 0
    vis_loc = set()
    if s.count('1') == 0:
        print((n // 2) + (n % 2))
    else:
        for i in range(1, n):
            if i - 1 == 0 and s[i-1] == '0' and s[i] == '0':
                res += 1
                vis_loc.add(i-1)
            elif i + 1 == n and s[i - 1] == '0' and s[i] == '0' and i - 1 not in vis_loc:
                res += 1
            elif (s[i-1] == '0') and (s[i] == '0') and i + 1 != n and (s[i+1] == '0') and (i - 1 not in vis_loc):
                res += 1
                vis_loc.add(i)
        print(res)