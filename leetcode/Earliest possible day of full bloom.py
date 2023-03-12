p_time = [10, 2, 3, 5]
g_time = [6, 11, 6, 3]

res = 0
s = 0
for i in range(len(p_time)):

    if res == 0:
        res = p_time[i] + g_time[i] + 1
        s = p_time[i]
    else:
        res -= res-s
        s += p_time[i]
        res += p_time[i] + g_time[i] + 1

# return res - 1
print(res - 1)
