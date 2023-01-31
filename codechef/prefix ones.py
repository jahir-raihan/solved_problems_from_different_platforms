# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()

    res = 0
    cnt = 0
    if s[0] == '1':
        i = 0
        while i < n and s[i] == '1':
            cnt += 1
            i += 1

    tmp_cnt = 0
    for i in range(cnt, n):
        if s[i] == '0':
            res = max(res, tmp_cnt)
            tmp_cnt = 0
        else:
            tmp_cnt += 1
    res = max(res, tmp_cnt)
    print(res + cnt)
