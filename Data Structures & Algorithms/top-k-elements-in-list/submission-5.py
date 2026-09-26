class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numF = {}
        kFinal = []
        for i in range(len(nums)):
            numF[nums[i]] = 1 + numF.get(nums[i], 0)
        numF = dict(sorted(numF.items(), key = lambda item:item[1], reverse=True))
        keys = list(numF.keys())
        for i in range(k):
            kFinal.append(keys[i])
        return kFinal