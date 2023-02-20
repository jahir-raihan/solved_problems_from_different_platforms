s = "CONTEST IS COMING".split()

max_len = 0
for w in s:
    max_len = max(max_len, len(w))
res = ['']*max_len
for word in s:
    for i in range(max_len):
        try:
            res[i] += word[i]
        except:
            res[i] += ' '
        res[i] = res[i].rstrip()


