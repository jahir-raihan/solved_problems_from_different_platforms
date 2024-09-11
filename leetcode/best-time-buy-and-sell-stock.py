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
        return res

# new
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i, j = 0, 1
        while j < len(prices):
            if prices[i] > prices[j]:
                i = j
                j = i + 1
            else:
                current_price = prices[j] - prices[i]
                max_profit = max_profit if max_profit > current_price else current_price
                j += 1
        return max_profit