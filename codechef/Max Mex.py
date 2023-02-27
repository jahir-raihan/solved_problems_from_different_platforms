for _ in range(int(input())):
    n, k = map(int, input().split())
    s = [int(x) for x in input().split()]
    mx = max(s)
    if mx - n < k:
        print(n+k)
    else:
        temp = [0]*(mx+1)
        for i in s:
            temp[i] = 1
        for i in range(mx+1):
            if temp[i] == 0:
                if k == 0:
                    print(i)
                    break
                k -= 1
