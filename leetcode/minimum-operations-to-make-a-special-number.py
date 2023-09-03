num = '2908305'
min_ops = len(num)
for rem in map(list, ('00', '25', '50', '75')):
    copy = list(num)
    ops = 0
    while copy and copy[-1] != rem[-1]:
        copy.pop(-1)
        ops += 1
    while len(copy) >= 2 and copy[-2] != rem[-2]:
        copy.pop(-2)
        ops += 1
    if copy[-2:] == rem:
        min_ops = min(min_ops, ops)
if '0' in num:
    min_ops = min(min_ops, len(num) - 1)
print(min_ops)