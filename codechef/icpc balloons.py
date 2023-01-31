# cook your dish here
for _ in range(int(input())):
    vis = {i: False for i in range(1, 8)}

    n = int(input())
    cnt = 0
    v_cont = 0
    a = map(int, input().split())
    for i in a:
        try:
            if vis[i] == False:
                vis[i] = True
                cnt += 1
                v_cont += 1
                if v_cont == 7:
                    break

        except:
            cnt += 1
    print(cnt)
