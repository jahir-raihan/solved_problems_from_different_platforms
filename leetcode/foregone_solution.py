for i in range(int(input())):
    n = input()
    if int(n) % 2 == 0:
        a = b = int(n) // 2
    else:
        a = b = int(n) / 2
        a = int(a) + 1
        b = int(b)
    ln = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
    s_a = str(a)
    cur_a = a
    cur_b = b
    for idx in range(len(s_a)):
        if '4' in str(cur_a) or '4' in str(cur_b):
            if s_a[idx] == '4':
                a_val = len(s_a) - idx
                c_v = ln[a_val - 1]
                cur_a += c_v
                cur_b -= c_v

    print(cur_a, cur_b)








