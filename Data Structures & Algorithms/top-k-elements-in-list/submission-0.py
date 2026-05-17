class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        kFinal = []
        for i in nums:
            countMap[i] = 0
        for i in range(len(nums)):
            countMap[nums[i]] += 1
        countMap = dict(sorted(countMap.items(), key=lambda item: item[1], reverse=True))
        countMapKeys = list(countMap.keys())
        print(countMap)
        print(countMapKeys)
        for i in range(k):
            kFinal.append(countMapKeys[i])
        return kFinal
        
        