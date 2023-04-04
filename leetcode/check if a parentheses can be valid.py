s = '))()))'
locked = '010100'
is_valid = True
stk = []
if s[0] == ')':
    is_valid = False
else:
    for p in s:
        if p == ')' and stk:
            stk.pop()
        elif p == '(':
            stk.append(p)
        else:
            is_valid = False
if is_valid:
    print(True)
else:
    