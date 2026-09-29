class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        window.add(nums[0])
        if k >= len(nums):
            k = len(nums)
        if k == 0:
            return False

        # slide r until window size k, so 1 to k-1. check if duplicate exists in seen each time we slide If exists, return true
        for r in range(1, k-1):
            if nums[r] in window:
                return True
            else:
                window.add(nums[r])

        # check if k-1 is in window since above for loop is exclusive and if k isnt 1.
        if nums[k-1] in window and k != 1:
            return True
        # otherwise add value at k-1 to window, make l = 0 and r = k
        window.add(nums[k-1])
        l = 0
        r = k
        # while r < len(nums)
        # if r < length and value at r is in window, return true,
        # else, add r to window, increment r, remove value at l, increment l
        while r < len(nums):
            if r < len(nums) and nums[r] in window:
                return True
            else:
                window.add(nums[r])
                r += 1
                window.remove(nums[l])
                l += 1
        # return false
        return False