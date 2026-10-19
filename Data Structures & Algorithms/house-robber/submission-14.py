class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n # dp[i] is the max amount of money you can rob up to house i including i
        dp[0] = nums[0]
        if n == 1:
            return dp[0]
        # at each house i, you can choose to rob this house and get max amount up to house i - 2, or get max amount up to i - 1
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[n-1]
        