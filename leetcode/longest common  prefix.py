strs = ['aa', 'aa']
ln = len(strs)
frq = {}
for string in strs:
    v = ''
    for ch in string:
        if ch not in v:
            try:
                frq[ch] += 1
            except:
                frq[ch] = 1
            v += ch
current_longest = ''
prev = None
for s in strs[0]:
    if s == prev:
        continue
    if frq[s] == ln:
        current_longest += s
        prev = s
    else:
        break

print(current_longest)
