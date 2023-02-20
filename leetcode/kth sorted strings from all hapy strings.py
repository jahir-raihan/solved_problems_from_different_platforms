class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        total = 3
        for _ in range(n - 1):
            total *= 2

        m_chars = ['a', 'b', 'c']
        if k > total:
            return ''

        prev_call = -1
        res = ''

        calls = 3
        k = k - 1
        while n > 0:
            single_part = total // calls
            call = k // single_part

            if call == 0:
                prev_call = 1 if prev_call == 0 else 0

            elif call == 1:
                if prev_call == -1 or prev_call == 2:
                    prev_call = 1
                else:
                    prev_call = 2

            else:
                prev_call = 2

            res += m_chars[prev_call]
            k -= single_part * call
            calls = 2
            total = single_part
            n -= 1
        return res
