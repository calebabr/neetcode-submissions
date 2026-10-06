class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums = sorted(nums)
        minDiff = 1000000
        currDiff = 1000000
        l = 0
        r = l + k - 1
        while (r < len(nums)):
            currDiff = nums[r] - nums[l]
            minDiff = min(currDiff, minDiff)
            l += 1
            r += 1
        return minDiff
    