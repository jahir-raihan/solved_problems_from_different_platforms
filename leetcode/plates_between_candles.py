s = "***|**|*****|**||**|*"
query = [[1,17],[4,5],[14,17],[5,11],[15,16]]
res = []
for i in query:
    le = ri = False
    l, r = i[0], i[1]
    while l < r:
        if not le:
            if s[l] == '|':
                le = True
            else:
                l += 1
        if not ri:
            if s[r] == '|':
                ri = True
            else:
                r -= 1
        if ri and le:
            break
    new_str = s[l+1:r].replace('|', '')
    res.append(len(new_str))


# This solution is too slow for millions inputs.

