class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # Figure out what half mid is in and adjust l, r based on that
            if nums[mid] > nums[mid + 1]: # minimum
                return nums[mid]
            elif nums[mid] > nums[r]: # we are in bigger half
                l = mid + 1
            else:
                r = mid - 1
        
