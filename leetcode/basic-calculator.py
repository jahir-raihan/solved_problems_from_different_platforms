class Solution:

    def __init__(self):
        self.s = None

    def calc(self, it):
        num, stack, sign = 0, [], "+"

        while it < len(self.s):
            if self.s[it].isdigit():
                num = num * 10 + int(self.s[it])
            elif self.s[it] in "+-":
                stack.append(num if sign == '+' else -num)
                num, sign = 0, self.s[it]
            elif self.s[it] == "(":
                num, j = self.calc(it + 1)
                it = j - 1
            elif self.s[it] == ")":
                stack.append(num if sign == '+' else -num)
                return sum(stack), it + 1
            it += 1
        stack.append(num if sign == '+' else -num)
        return sum(stack)

    def calculate(self, s):

        self.s = s
        return self.calc(0)