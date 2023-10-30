t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    cnt_1, ans = 0, 0
    res = []
    for i in range(n - 1, -1, -1):
        if s[i] == "1":
            cnt_1 += 1
        else:
            ans += cnt_1
            res.append(ans)
    print(*res+[-1] * (n - len(res)))