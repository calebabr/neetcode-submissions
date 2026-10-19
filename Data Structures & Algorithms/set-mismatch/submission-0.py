class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numFreq = {}
        for i in range(len(nums)):
            numFreq[nums[i]] = 1 + numFreq.get(nums[i], 0)
        for num in numFreq:
            if numFreq[num] > 1:
                return [num, num+1]
        return None