class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return 0
        freqDict = {}
        pairs = 0
        for i in range(len(nums)):
            freqDict[nums[i]] = 1 + freqDict.get(nums[i], 0)

        for num in freqDict:
            pairs += (freqDict[num] - 1) * (freqDict[num]) // 2
        return pairs
        