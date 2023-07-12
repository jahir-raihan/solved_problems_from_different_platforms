s = 'PAYPALISHIRING'
length = len(s)
rows = 3
gap = rows - 2
lst = [[0 for _ in range(length//2)] for _ in range(rows)]
counter = 0
for i in range(0, length, rows+gap):
    tmp_str = s[i:i+rows]
    for j in range(len(tmp_str)):
        lst[j][counter] = tmp_str[j]
    counter += gap + 1

counter = 1
for i in range(rows, length, rows+gap):
    tmp_str = s[i:i+gap]
    cur_idx = rows-2
    for j in range(len(tmp_str)):
        lst[cur_idx][counter] = tmp_str[j]
        cur_idx -= 1
        counter += 1
    counter += 1



res = ''
for i in lst:
    for j in i:
        if j != 0:
            res += j
print(res)