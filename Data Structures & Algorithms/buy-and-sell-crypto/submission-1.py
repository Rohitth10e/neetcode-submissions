class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell_price = float('inf')
        max_profit = float('-inf')

        for price in prices:
            sell_price = min(price, sell_price)
            profit = price - sell_price
            max_profit = max(max_profit, profit)
        return max_profit