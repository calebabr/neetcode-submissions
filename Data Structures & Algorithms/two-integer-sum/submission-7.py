class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = 0
        indexMap = {}
        for i, j in enumerate(nums):
            indexMap[j] = i
        for i, j in enumerate(nums):
            diff = target - j
            if diff in indexMap and indexMap[diff] != i:
                return [i, indexMap[diff]]
        print(indexMap)
        return [0, 1]