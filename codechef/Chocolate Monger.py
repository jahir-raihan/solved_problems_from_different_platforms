# cook your dish here
for i in range(int(input())):
    n, x = map(int, input().split())
    lst = list(map(int, input().split()))
    s_lst = set(lst)
    if len(s_lst) <= n - x:
        print(len(s_lst))
    else:
        tmp = len(lst) - len(s_lst)
        t = x - tmp
        print(len(s_lst) - t)

