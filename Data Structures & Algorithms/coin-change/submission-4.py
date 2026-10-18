class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0.0
        for amt in range(1, amount+1):
            for cVal in coins:
                if amt - cVal >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - cVal])
        if dp[amount] == float('inf'):
            return -1
        return int(dp[amount])