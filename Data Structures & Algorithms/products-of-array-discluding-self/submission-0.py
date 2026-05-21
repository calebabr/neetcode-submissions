class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefProd = [1] * len(nums)
        sufProd = [1] * len(nums)
        for i in range(1, len(nums)):
            prefProd[i] = prefProd[i-1] * nums[i-1]
        for i in range(len(nums)- 2, -1, -1):
            sufProd[i] = sufProd[i+1] * nums[i+1]
        print(nums)
        for i in range(len(nums)):
            nums[i] = prefProd[i] * sufProd[i]
        print(prefProd)
        print(sufProd)
        return nums
        