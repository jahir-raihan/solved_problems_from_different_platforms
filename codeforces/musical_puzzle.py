for _ in range(int(input())):
    n = int(input())
    s = input()
    dic = {}
    cnt = 0
    for i in range(n - 1):
        try:
            tmp = dic[s[i]+s[i+1]]
            continue
        except:
            dic[s[i]+s[i+1]] = 0
            cnt += 1
    print(cnt)