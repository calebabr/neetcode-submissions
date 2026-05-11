class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = buy - sell
        # buy index HAS to be to the left of sell index
        # Assume minimum buying price has to be first item. Iterate
        # through prices and calculate max profit and updating minimum buying price
        maxProfit = 0
        minBuy = prices[0]

        for i in prices:
            maxProfit = max(maxProfit, i - minBuy)
            minBuy = min(minBuy, i)
        return maxProfit
        # for i in indexList:

            # print(i)
        