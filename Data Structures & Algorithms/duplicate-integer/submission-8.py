class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {}
        for i, j in enumerate(nums):
            countMap[j] = 0
        for i in range(len(nums)):
            countMap[nums[i]] += 1
        for x in countMap.values():
            if x > 1:
                return True
        # print(indMap)
        return False

        