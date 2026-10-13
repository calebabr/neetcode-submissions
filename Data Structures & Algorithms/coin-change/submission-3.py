class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0.0
        for i in range(1, amount + 1):
            for coinVal in coins:
                if i - coinVal >= 0: # aka this is a valid coin to use
                    dp[i] = min(dp[i], 1 + dp[i - coinVal])
        if dp[amount] == float('inf'):
            return -1
        return int(dp[amount])