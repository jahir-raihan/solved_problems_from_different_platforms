banned = [176,36,104,125,188,152,101,47,51,65,39,174,29,55,13,138,79,81,175,178,42,108,24,80,183,190,123,20,139,22,140,62,58,137,68,148,172,76,173,189,151,186,153,57,142,105,133,114,165,118,56,59,124,82,49,94,8,146,109,14,85,44,60,181,95,23,150,97,28,182,157,46,160,155,12,67,135,117,2,25,74,91,71,98,127,120,130,107,168,18,69,110,61,147,145,38]

n = 3016
maxSum = 240
if n > maxSum:
    n = maxSum
range_list = [i for i in range(1, n + 1)]
banned = sorted(set(banned))

banned_vals = []
i = 0
while i < len(banned) and banned[i] <= n:
    banned_vals.append(banned[i])
    i += 1
for val in banned_vals:
    if val in range_list:
        range_list.remove(val)

count = 0
i = len(range_list)
for j in range(len(range_list)):
    if maxSum == 0 or maxSum - range_list[j] < 0:
        break
    else:
        count += 1
        maxSum -= range_list[j]
print(count)

