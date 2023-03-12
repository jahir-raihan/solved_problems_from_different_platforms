s = "ab"
t = "baab"
mx = 0
cnt = 0
l = len(s)
for i in t:
    if i in s and s.index(i)+1 >= mx:
        mx = s.index(i)+1
        cnt += 1
#   return l == cnt
print(l == cnt)

