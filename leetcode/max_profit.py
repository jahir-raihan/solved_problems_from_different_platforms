prices = [6, 4, 5, 3, 4, 3, 2]
mx_c = 0
mx_f = 0
for i in range(1, len(prices)):
    mx_c = max(0, mx_c + prices[i] - prices[i - 1])
    mx_f = max(mx_c, mx_f)
"""
Next challenges:

Maximum Subarray
Best Time to Buy and Sell Stock II
Best Time to Buy and Sell Stock III
Best Time to Buy and Sell Stock IV
Best Time to Buy and Sell Stock with Cooldown
Sum of Beauty in the Array
Maximum Difference Between Increasing Elements
Maximum Profit From Trading Stocks

"""