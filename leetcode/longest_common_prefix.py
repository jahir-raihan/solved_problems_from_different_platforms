strs = ["flower", "flow", "flight"]
res = ''
for i in range(len(strs[0])):
  for s in strs:
    if i == len(s) or s[i] != strs[0][i]:
      break # return True
  res += strs[0][i]