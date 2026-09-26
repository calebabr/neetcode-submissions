class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]
        for price in prices:
            maxProfit = max(price - minBuy, maxProfit)
            minBuy = min(price, minBuy)
        return maxProfit