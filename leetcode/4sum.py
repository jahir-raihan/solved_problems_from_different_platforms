res = []
v = 9999999999
lst = [2,2,2,2]
t = 8

for n in range(len(lst)-3):
    if n > 0 and lst[n] == lst[n - 1]:
        continue
    i = n + 1
    while i < len(lst) - 2:
        if i > n + 1 and lst[i] == lst[i-1]:
            i += 1
            continue
        j, k = i+1, len(lst)-1

        while j < k:
            tmp = lst[n] + lst[i] + lst[j] + lst[k]
            if tmp > t:
                k -= 1
            elif tmp < t:
                j += 1
            else:
                res.append([lst[n], lst[i], lst[j], lst[k]])
                j += 1
                while k > j > i + 1 and lst[j - 1] == lst[j]:
                    j += 1
        i += 1

print(res)