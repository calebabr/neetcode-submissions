class Solution:
    def jump(self, nums: List[int]) -> int:
        currEnd = 0
        jumps = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i]) # farthest index we can jump to from here
            if i == currEnd: # We've reached the farthest we can jumnp to, time to recalculate
                jumps += 1
                currEnd = farthest
        return jumps