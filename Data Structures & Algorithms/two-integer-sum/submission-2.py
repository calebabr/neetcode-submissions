class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = 0
        indexMap = {}
        for i, j in enumerate(nums):
            indexMap[j] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indexMap and diff != nums[i]:
                return [indexMap[i], i]
        print(indexMap)
        return [-1, -1]