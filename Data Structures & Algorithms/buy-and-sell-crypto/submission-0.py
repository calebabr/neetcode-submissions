class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = buy - sell
        # buy index HAS to be to the left of sell index
        # Dynamic programming
        maxProfit = 0
        minBuy = prices[0]

        for i in prices:
            maxProfit = max(maxProfit, i - minBuy)
            minBuy = min(minBuy, i)
        return maxProfit
        # for i in indexList:

            # print(i)
        