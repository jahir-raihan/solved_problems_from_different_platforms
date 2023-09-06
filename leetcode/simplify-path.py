path = "/.././tqCEe/..///L/../../././//../../../JGF/../ZUFaY/.///wMzVK//."

prev = None
remove_slashes = ''
for w in path:
    remove_slashes += '' if prev == w and w == '/' else w
    prev = w

sep_path = [i for i in remove_slashes.split('/') if i != '' and i != '.']
res_stk = []

for p in sep_path:
    if p == '..':
        if res_stk:
            res_stk.pop()
    else:
        res_stk.append(p)

res = ''
for p in res_stk:
    res += '/' + p
print(res if res != '' else '/')
