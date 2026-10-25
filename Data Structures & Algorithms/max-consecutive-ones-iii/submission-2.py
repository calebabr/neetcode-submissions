class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        zeroes = 0
        best = 0
        for r, num in enumerate(nums):
            if num == 0:
                zeroes += 1
            while zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1
            best = max(best, r- l + 1)
        return best