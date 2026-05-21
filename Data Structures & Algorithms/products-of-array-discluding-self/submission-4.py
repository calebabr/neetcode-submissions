class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefProd = [1] * len(nums)
        sufProd = [1] * len(nums)
        for i in range(1, len(nums)):
            prefProd[i] = prefProd[i-1] * nums[i-1]
        # nums = 1 2 4 6
        # i = 1
        # prefProd 1 1 1 1
        # i = 2
        # prefProd 1 1 2 1
        # i = 3
        # prefProd 1 1 2 8
        for i in range(len(nums)- 2, -1, -1):
            sufProd[i] = sufProd[i+1] * nums[i+1]
        # print(nums)
        for i in range(len(nums)):
            nums[i] = prefProd[i] * sufProd[i]
        # print(prefProd)
        # print(sufProd)
        return nums
        