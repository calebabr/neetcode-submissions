class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * (n+1)
        dp[0] = 0.0
        for i in range(0, n-1):
            for j in range(i + 1, min(i + nums[i], n-1) + 1):
                dp[j] = min(dp[j], dp[i] + 1)
        return int(dp[n-1])