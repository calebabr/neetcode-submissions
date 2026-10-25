class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        currSum = 0
        prefSum = {0:1} # for the empty prefix

        for num in nums:
            currSum += num
            diff = currSum - k
            
            count += prefSum.get(diff, 0)
            prefSum[currSum] = 1 + prefSum.get(currSum, 0)
        
        return count