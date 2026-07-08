class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        doubNums = [0] * len(nums) * 2
        for i in range(len(nums)):
            doubNums[i] = doubNums[len(nums) + i] = nums[i]
        return doubNums