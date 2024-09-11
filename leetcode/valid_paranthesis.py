s = '()'
stk = []
for i in s:
    if i in ['(', '[', '{']:
        stk.append(i)
    elif (i == ']' and stk[-1] == '[') or (i == '}' and stk[-1] == '{') or (i == ')' and stk[-1] == '('):
        continue
    else:
        break


# Updated
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mapper = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in (')', ']', '}') and stk and mapper[i] == stk[-1]:
                stk.pop(-1)
            else:
                stk.append(i)

        return not stk