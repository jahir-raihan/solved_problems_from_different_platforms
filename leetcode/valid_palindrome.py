s = "0A man, a plan, a canal: Panama"

c = ''
for i in s:
    if i.isnumeric() or i.isalpha():
        c += i.lower()

i, j = 0, len(c) - 1
while i < j:
    if c[i] != c[j]:
        res = False
        break

