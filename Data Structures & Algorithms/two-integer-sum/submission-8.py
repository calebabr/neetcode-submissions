class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = 0
        indexDict = {}
        # Make indexDict a 
        for i, v in enumerate(nums):
           indexDict[v] = i
        for i, v in enumerate(nums):
            diff = target - v
            if diff in indexDict and i != indexDict[diff]:
                return[i, indexDict[diff]]
        return [0, 1] 
