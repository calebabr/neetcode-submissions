class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currEnd = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= currEnd:
                currEnd = i

        return currEnd == 0