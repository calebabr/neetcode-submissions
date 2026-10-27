class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        
        def bt(i, runSum):
            nonlocal total
            total += runSum

            for j in range(i, len(nums)):
                bt(j+1, runSum ^ nums[j])
        
        bt(0, 0)
        return total