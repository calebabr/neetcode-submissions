class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pProd = [1] * len(nums)
        sProd = [1] * len(nums)
        # Calculate prefix
        for i in range(1, len(nums)):
            pProd[i] = pProd[i-1] * nums[i - 1]
        # Calculate suffix
        for i in range(len(nums) - 2, -1, -1):
            sProd[i] = sProd[i + 1] * nums[i + 1]
        # Update nums
        for i in range(len(nums)):
            nums[i] = pProd[i] * sProd[i]
        return nums