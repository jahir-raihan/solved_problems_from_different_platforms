s = '()'
stk = []
for i in s:
    if i in ['(', '[', '{']:
        stk.append(i)
    elif (i == ']' and stk[-1] == '[') or (i == '}' and stk[-1] == '{') or (i == ')' and stk[-1] == '('):
        continue
    else:
        break

