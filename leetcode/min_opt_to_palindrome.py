s = 'welcome'
cnt = 0
i, j = 0, len(s) - 1
while i <= j:
    cnt += 1 if s[i] != s[j] else 0
    i += 1
    j -= 1
print(cnt)