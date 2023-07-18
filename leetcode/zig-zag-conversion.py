s = 'ABC'
length = len(s)
rows = 1
columns = rows - 2
lst = [[0 for _ in range(length)] for _ in range(rows+1)]

i, turn = 0, 0
cur_idx = 0
while i < length:
    if turn == 0:
        tmp_str = s[i: i+rows]
        turn = 1

        for j in range(len(tmp_str)):
            lst[j][cur_idx] = tmp_str[j]
        cur_idx += 1
        i += rows

    elif turn == 1 and columns > 0:
        tmp_str = s[i: i+columns]
        turn = 0

        k = columns
        for j in range(len(tmp_str)):
            lst[k][j+cur_idx] = tmp_str[j]
            k -= 1
        cur_idx += columns
        i += columns
    else:
        turn = 0

res = ''
for l in lst:
    for c in l:
        res += c if c != 0 else ''

print(res)