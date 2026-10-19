class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        count = 0
        for num in nums:
            numSet.add(num)
        for i in range(len(nums)):
            if (nums[i] + 1) in numSet:
                count += 1
        print(numSet)
        return count