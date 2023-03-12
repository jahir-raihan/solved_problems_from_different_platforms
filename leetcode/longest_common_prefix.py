strs = ["flower", "flow", "flight"]
l = strs[0]
for i in range(1, len(strs)):
    l = [val for val in strs[i] if val in l]
print(''.join(l))