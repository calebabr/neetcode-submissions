class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefSum = [0] * len(nums)
        for i in range(1, len(nums)):
            prefSum[i] = prefSum[i-1] + nums[i - 1]
        count = 0
        targDict = {}
        for i in range(len(nums)):
            targDict[prefSum[i]] = 1 + targDict.get(prefSum[i], 0)
            target = prefSum[i] + nums[i] - k
            if target in targDict:
                count += targDict[target]
            else:
                count += 0
            

        # print(prefSum)
        return count