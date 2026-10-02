class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        if k >= len(nums):
            k = len(nums)
        if k == 0:
            return False
        # build window size 
        # in between phase, check 
        l = 0
        window.add(nums[l])
        r = 1
        while r < len(nums):
            if nums[r] in window:
                return True
            window.add(nums[r])
            r += 1
            if (r - l) > k:
                window.remove(nums[l])
                l += 1
        return not (nums[len(nums) - 1] in window)