class Solution:
    def jump(self, nums: List[int]) -> int:
        currEnd = 0
        jumps = 0
        farthest = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if i == currEnd:
                jumps += 1
                currEnd = farthest
        return jumps