class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return 0
        
        freqDict = {}
        totalPairs = 0
        for i in nums:
            freqDict[i] = 1 + freqDict.get(i, 0)
        for num in freqDict:
            n = freqDict[num]
            totalPairs += ((n) * (n-1)) // 2
        return totalPairs