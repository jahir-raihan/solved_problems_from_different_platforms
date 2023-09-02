s1 = 'abcd'
s2 = 'abcd'
s1 = [i for i in s1]
l = len(s1)
res = False
for i in range(l):

    if i < 2 and s1[i] != s2[i] and s1[i + 2] != s2[i]:
        break
    elif i < 2 and s1[i] != s2[i] and s1[i + 2] == s2[i]:
        s1[i], s1[i + 2] = s1[i + 2], s1[i]
    else:
        if s1[i] != s2[i]:
            break
