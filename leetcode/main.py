s = 'ccccccccc'
res = ''
max_len = 0

for i in range(len(s)):
    l, r = i, i
    ms = False
    if r+1 < len(s) and s[l] == s[r+1]:
        r += 1
        ms = True
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if (r-l + 1) > max_len:
            res = s[l:r+1]
            max_len = r - l + 1
        l -= 1
        if not ms:
            r += 1
print(res)