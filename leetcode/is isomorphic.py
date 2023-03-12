s = "egg"
t = "add"

m1 = {}
m2 = {}
c = 0
l = len(s)
for i in range(l):
    if s[i] in m1:
        if m1[s[i]] != t[i]:
            break
        else:
            c += 1

    elif s[i] not in m1 and t[i] not in m2:
        m1[s[i]] = t[i]
        m2[t[i]] = s[i]
        c += 1
    else:
        break
#   return l == c
print(l == c)

