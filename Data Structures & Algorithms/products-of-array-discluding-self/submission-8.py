class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefProd = [1] * len(nums)
        sufProd = [1] * len(nums)
        for p in range(1, len(nums)):
            prefProd[p] = prefProd[p - 1] * nums[p - 1]
        for s in range(len(nums) - 2, -1, -1):
            sufProd[s] = sufProd[s + 1] * nums[s + 1]
        for i in range(len(nums)):
            nums[i] = prefProd[i] * sufProd[i]
        return nums