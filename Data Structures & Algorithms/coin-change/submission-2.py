class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coinSet = set(coins)
        # n = len(coins)
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for amt in range(1, amount + 1):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])

        if dp[amount] == float('inf'):
            return -1
        return int(dp[amount])