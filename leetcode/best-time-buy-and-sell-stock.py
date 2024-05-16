class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dic = defaultdict(int)

        l = len(prices)

        res = 0
        cur_val = prices[0]
        for i in range(l):
            if prices[i] > cur_val:
                res = max(res, prices[i] - cur_val)
            else:
                cur_val = prices[i]
        return r