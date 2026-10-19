class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currEnd = len(nums) - 1
        for i in range(currEnd, -1, -1):
            if i + nums[i] > currEnd: # We update currEnd based on whether or not we can jump to it. This way we only need to see if we can jump to a specific spot from anywhere in array and update that spot if so
                currEnd = i
        return currEnd == 0
            