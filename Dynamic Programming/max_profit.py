# Solved on 22/07/2024
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

# IMPORTANT: 
# THE PROBLEM DESCRIPTION STATES fee IS A TRANSACTION FEE (I.E. FOR BOTH BUYING AND SELLING), 
# IT REALLY IS ONLY A SELLING FEE.

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # Tuple (x,y) where x is the maximal amount of profit we end up with if we end the previous
        # day owning a stock, and y the maximal amount of profit we end the prevoius day without a stock.
        # We start with 0 profit.
        profits = (0,0)
        for i in range(n):
            # Either buy a stock, subtracting the cost from profit after selling, or hold the existing stock.
            buy_profit = -prices[0] if i == 0 else max(profits[1] - prices[i], profits[0])
            # Either sell the existing stock, adding it's value to the profit when owning a stock and subtracting the
            # fee, or don't buy a stock and keep the previous profit.
            # On the 0th day selling a stock has no meaning.
            sell_profit = 0 if i == 0 else max(profits[0] + prices[i] - fee, profits[1])
            profits = (buy_profit, sell_profit)
        return max(profits)
