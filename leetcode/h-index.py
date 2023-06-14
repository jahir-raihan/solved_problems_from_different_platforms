citations  = [3, 11, 13]

citations.sort()
res = 0
length = len(citations)
for i in range(length):
    if length - i >= citations[i]:
        res = citations[i]
    else:
        res = max(res, length-i)
        break


print(res)