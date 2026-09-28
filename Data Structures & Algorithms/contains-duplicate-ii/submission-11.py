class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        window.add(nums[0])
        if k >= len(nums):
            k = len(nums)
        if k == 0:
            return False
        
        for r in range(1, k-1): # slide r until we have window size k
            if nums[r] not in window:
                window.add(nums[r])
            else:
                return True
        
        # now slide the entire window where l is at 0 and r is at k changing both. remove value at l pointer and add value at r if its not in set. otherwise, return value at new r and the index in the set that it was equal to
        if nums[k-1] in window and k!= 1:
            return True
        window.add(nums[k-1])
        l = 0
        r = k
        while r < len(nums):
            if r < len(nums) and nums[r] in window:
                return True
            window.add(nums[r])
            r += 1
            window.discard(nums[l])
            l += 1
        return False
