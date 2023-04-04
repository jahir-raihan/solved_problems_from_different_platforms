s = input()
s = s.replace('+', ' ')
s = list(map(int, s.split()))
s.sort()
res = str(s[0])
for v in range(1, len(s)):
    res += '+'
    res += str(s[v])
print(res)
