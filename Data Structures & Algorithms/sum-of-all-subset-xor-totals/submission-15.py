class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        path = []

        def bt(i):
            nonlocal total

            x = 0
            for num in path:
                x ^= num
            total += x

            for j in range(i, len(nums)):
                path.append(nums[j])
                bt(j + 1)
                path.pop()
        
        bt(0)
        return total