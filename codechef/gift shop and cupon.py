import math

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    cnt = 0
    for i in a:
        if k - i < 0 and 0 < k >= math.ceil(i / 2):
            cnt += 1
            break
        elif k >= i:
            k -= i
            cnt += 1
    print(cnt)




