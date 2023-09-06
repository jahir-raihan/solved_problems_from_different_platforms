class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        operands = '+-*/'
        for oprnd in tokens:
            if oprnd in operands:
                val1 = stk.pop()
                val2 = stk.pop()
                val = (val2 + val1 if oprnd == '+' else val2 - val1 if oprnd == '-' else val2 * val1 if
                oprnd == '*' else float(val2) / val1)

                stk.append(int(val))
            else:
                stk.append(int(oprnd))

        return stk[0]
