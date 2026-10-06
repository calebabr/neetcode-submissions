class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numFreq = {}
        numSet = set()
        res = [0,0] # dup missing
        for i in range(len(nums)):
            numSet.add(nums[i])
        for i in range(1, len(nums) + 1):
            numFreq[i] = 0
        print(numFreq)
        for i in range(len(nums)):
            numFreq[nums[i]] += 1
        print(numFreq)
        for num in numFreq:
            if numFreq[num] == 0:
                res[1] = num
            if numFreq[num] > 1:
                res[0] = num
        return res
