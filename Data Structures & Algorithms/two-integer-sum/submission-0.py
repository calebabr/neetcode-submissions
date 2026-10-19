class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create hashmap of valueInNum : indexOfValue
        diff = 0
        indexList = {}
        for i, j in enumerate(nums): # j is the value at i
            indexList[j] = i 
        for h, k in enumerate(nums):
            diff = target - k
            if diff in indexList and indexList[diff] != h:
                return [h, indexList[diff]]
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     for j in range(i+1, len(nums)):
        #         if (diff == nums[j]):
        #             return [i, j]
        return [0, 1]
        