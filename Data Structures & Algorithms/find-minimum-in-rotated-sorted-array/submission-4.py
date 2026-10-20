class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        # nums[l] always greater than nums[r] if rotated. if less than, return the min betwee current res and nums[l]
        # find mid. res is the smaller between current res and val at mid. if val at mid is greater than nums[l], mid is in the greater half. shrink by moving l to mid + 1. else, r to mid - 1 because mid is in smaller half
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res