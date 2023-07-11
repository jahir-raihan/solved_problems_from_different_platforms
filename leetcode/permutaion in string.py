s1 = 'adc'
s2 = 'dcda'

s = sorted(s1)
for i in range(len(s2) - len(s) + 1):
    t = sorted(s2[i:i+len(s)])
    if s == t:
        break
