class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        diff = 0
        for i, j in enumerate(nums):
            indexMap[j] = i
        for i, j in enumerate(nums):
            diff = target - j
            if diff in indexMap and indexMap[diff] != i:
                return [i, indexMap[diff]]
        return [0, 1]
