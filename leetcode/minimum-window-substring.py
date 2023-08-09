s = "ADOBECODEBANC"
t = "ABC"

dic = {}
target_count = 0
for c in t:
    try:
        dic[c] += 1
    except:
        dic[c] = 1
    target_count += 1

res = 9999999999
final_res = ''
i = 0
while i < len(s):

    dic_copy = dic.copy()
    j = i
    c_target_count = target_count
    second_found_val = None
    while c_target_count > 0 and j < len(s):
        try:
            val = dic_copy[s[j]]
            if val > 0:
                dic_copy[s[j]] -= 1
                c_target_count -= 1

                if second_found_val is None and j > i:
                    second_found_val = j
        except:
            pass
        j += 1

    if j - i < res and c_target_count == 0:
        final_res = s[i:j]
        res = j - i

    if second_found_val:
        i = second_found_val
    else:
        i += 1

print(final_res)