def get_or_put(c):
    try:
        dic[c] += 1
    except:
        dic[c] = 1


for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    dic = {}
    cnt = 0

    for ch in s:
        char = ch.lower() if ch.isupper() else ch.upper()
        try:
            if dic[char] > 0:
                dic[char] -= 1
                cnt += 1
            else:
                get_or_put(ch)
        except:
            get_or_put(ch)

    for key, v in dic.items():
        if k == 0:
            break
        if k > 0 and v > 1:
            r = min(v // 2, k)
            k -= r
            cnt += r
    print(cnt)

