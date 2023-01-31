# cook your dish here
for _ in range(int(input())):
    input()
    t = map(int, input().split())
    dic = {}
    for i in t:
        try:
            dic[i] += 1
        except:
            dic[i] = 1
    mx = 0
    for k, v in dic.items():
        mx = mx if mx > k + v - 1 else k + v - 1
    print(mx)


