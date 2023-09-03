low = 1200
high = 1230

count = 0
for i in range(low, high+1):
    s_i = str(i)
    mid = len(s_i) // 2
    first_sum = sum([int(i) for i in s_i[:mid]])
    second_sum = sum([int(i) for i in s_i[mid:]])
    if len(s_i) % 2 == 0 and first_sum == second_sum:
        count += 1
print(count)