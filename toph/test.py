# import math
#
# t = 1
#
# for _ in range(t):
#     h, x, y1, y2, k = 117, 21, 35, 10, 2#map(int, input().split())
#
#     x = math.ceil(h / x)
#     print("x", x)
#     y = math.ceil(h / y1)
#     print('y', y)
#     if y > k:
#         tmp = math.ceil((h - (k * y1)) / y2)
#         y = (y - 1) + tmp
#
#     print(min(x, y))


t = 1

# for _ in range(t):
#     n = 4
#     s = ['x', 'x', 'y', 'y']
#     remove = None
#
#     for i in range(n - 2, -1, -1):
#         if ord(s[i]) > ord(s[i + 1]):
#             remove = i
#     s.pop(remove)
#     print(''.join(s[:-1]))

# x, i = 22, 0
#
# for i in range(0, x, 5):
#     print('Real')
#     if i == 5 or i == 15:
#         continue
#     print("madrid")
t = 1

for _ in range(t):
    n, m = 3, 2
    a = [3, 2, 4]
    shadow = [0] * n
    res = 0
    for idx, val in enumerate(a):
        if val >= m:
            shadow[idx] = 1
            res += 1

    i = 0
    while i < n:
        if shadow[i] == 0:
            cur_res = a[i]
            k = i + 1
            while k < n and shadow[k] != 1:
                if cur_res + a[k] >= m:
                    res += 1
                    i = k + 1
                    break
                else:
                    cur_res += a[k]
                    k += 1
            else:
                i += 1
        else:
            i += 1
    print(res)