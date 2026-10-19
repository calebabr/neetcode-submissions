class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        count = 0
        if len(nums) == 1:
            return 1
        for num in nums:
            numSet.add(num)
        if len(numSet) == 1:
            return 1
        for i in range(len(nums)):
            if (nums[i] + 1) in numSet:
                count += 1
        print(numSet)
        return count