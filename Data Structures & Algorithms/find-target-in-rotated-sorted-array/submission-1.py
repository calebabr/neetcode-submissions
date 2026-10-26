class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # in left sorted
            if nums[l] <= nums[mid]:
            # Check if target is in this side.
                if target > nums[mid] or target < nums[l]: # need to search right
                    l = mid + 1
                else:
                    r = mid - 1
                
            else: # right portion is sorted
            # Check if target is in this side
                if target < nums[mid] or target > nums[r]: # Need to search left
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1