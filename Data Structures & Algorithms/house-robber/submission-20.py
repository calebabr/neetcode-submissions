class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # dp = [0] * n # dp[i] is the max amount of money you can rob up to house i including i
        prev2 = nums[0]
        prev = max(nums[0], nums[1])
        curr = prev
        # at each house i, you can choose to rob this house and get max amount up to house i - 2, or get max amount up to i - 1
        for i in range(2, n):
            curr = max(nums[i] + prev2, prev)
            prev2 = prev
            prev = curr

        return curr
        