class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        currSum = 0
        prefSum = {0:1}

        for num in nums:
            currSum += num
            diff = curSum - k
            
            count += prefSum.get(diff, 0)
            prefSum[currSum] = 1 + prefSum.get(curSum, 0)
        
        return count