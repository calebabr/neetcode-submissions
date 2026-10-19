class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [0] * (n)
        twoHouse = nums[0]
        if n == 1:
            return twoHouse
        curr = 0
        
        prevHouse = max(nums[0], nums[1])
        for i in range(2, n):
            curr = max(twoHouse + nums[i], prevHouse)
            twoHouse = prevHouse
            prevHouse = curr
        
        return curr