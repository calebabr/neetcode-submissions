class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        iDict = {}
        for i, v in enumerate(nums):
            iDict[v] = i
        # print(iDict)
        # print(nums)
        for i, v in enumerate(nums):
            diff = target - v
            if diff in iDict and i != iDict[diff]:
                return [i, iDict[diff]]
        return [-1, -1]