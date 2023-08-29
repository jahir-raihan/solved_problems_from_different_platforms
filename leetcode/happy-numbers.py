class Solution:
    def isHappy(self, n: int) -> bool:
        is_seen = {}

        while n != 1:
            tmp_sum = [int(x) for x in str(n)]
            total_sum = sum([z**2 for z in tmp_sum])
            n = total_sum

            try:
                tmp = is_seen[n]
                return False
            except:
                is_seen[n] = 0
        return True
