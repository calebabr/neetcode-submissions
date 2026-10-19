class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        indMap = {}
        for i, j in enumerate(nums):
            indMap[j] = i
        for i in nums:
            if i in indMap and indMap[i] != nums.index(i):
                return True
        print(indMap)
        return False

        