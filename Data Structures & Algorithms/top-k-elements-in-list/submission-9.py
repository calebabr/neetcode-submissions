class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numF = {}
        kFinal = []
        # Get a num frequency dict
        for i in range(len(nums)):
            numF[nums[i]] = 1 + numF.get(nums[i], 0)
        # reverse order the dict and turn keys into a list
        numF = dict(sorted(numF.items(), key=lambda item:item[1], reverse=True))
        numKeys = list(numF.keys())
        # iterate i 0 to k (not including k aka for loop), append each value at keys list to kFinal
        for i in range(k):
            kFinal.append(numKeys[i])
        return kFinal