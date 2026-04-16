class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float('inf')
        max_profit = float('-inf')
    
        for price in prices:
            buy_price = min(price, buy_price)
            sell_price = price - buy_price
            max_profit = max(max_profit, sell_price)
        return max_profit