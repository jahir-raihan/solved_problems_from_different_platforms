s = "barfoothefoobarman"
words = ["bar", "foo"]
h_map = {}

for word in words:
    try:
        h_map[word] += 1
    except:
        h_map[word] = 1

ans = []

i = 0
j = (len(words[0])*len(words)) - 1

while j < len(s):
    a = i
    b = i + len(words[0]) - 1
    tmp = h_map.copy()
    freq = len(words)

    while b <= j:
        try:
            val = s[a:b+1]
            tmp[val] -= 1
            if tmp[val] <= 0:
                del tmp[val]
            freq -= 1
        except:
            pass

        a = b + 1
        b += len(words[0])

    if freq == 0:
        ans.append(i)
    i += 1
    j += 1
print(ans)
