class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        currLength = 1
        currNum = 0
        bestLength = 0
        for num in nums:
            if num not in numSet:
                numSet.add(num)
            
        for num in numSet:
            # ONly start at possible beginning of sequences
            if (num - 1) not in numSet:
                currNum = num + 1
                currLength = 1
                while currNum in numSet:
                    currNum += 1
                    currLength += 1
                bestLength = max(currLength, bestLength)
        return bestLength
        