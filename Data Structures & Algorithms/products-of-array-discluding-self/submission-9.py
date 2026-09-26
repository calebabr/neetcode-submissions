class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Calculate prefix prod and suffix prod
        pProd = [1] * len(nums)
        sProd = [1] * len(nums)
        for i in range(1, len(pProd)):
            pProd[i] = nums[i-1] * pProd[i - 1]
        for i in range(len(sProd) - 2, -1, -1):
            sProd[i] = nums[i + 1] * sProd[i + 1]
        for i in range(len(sProd)):
            nums[i] = sProd[i] * pProd[i]
        return nums
