# cook your dish here
for i in range(int(input())):
    n = int(input())
    res = -1

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    mx_post = -1
    mx_comment = -1

    for k in range(n):
        if a[k] > mx_post:
            mx_post = a[k]
            res = k
            mx_comment = b[k]

        elif a[k] == mx_post and mx_comment < b[k]:
            mx_post = a[k]
            mx_comment = b[k]
            res = k
    print(res + 1)