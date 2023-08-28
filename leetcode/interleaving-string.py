s1 = 'aabcc'
s2 = 'dbbca'
s3 = 'aadbbcbcac'

i = 0
j = 0

idx = 0
res = True
while idx < len(s3):
    if i < len(s1) and s3[idx] == s1[i]:
        idx += 1
        i += 1
    elif j < len(s2) and s3[idx] == s2[j]:
        idx += 1
        j += 1
    else:
        res = False
        break

print(res)