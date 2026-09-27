class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        best = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                best = max(count, best)
                count = 0
        best = max(count, best)
        return best