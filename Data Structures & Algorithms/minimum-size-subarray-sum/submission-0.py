class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum = 0
        l = 0
        res = float('inf')
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                res = min(r-l+1, res)
                currSum -= nums[l]
                l += 1
        
        if res == float('inf'):
            return 0
        return res