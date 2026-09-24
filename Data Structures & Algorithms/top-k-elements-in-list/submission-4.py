class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = {}
        kFinal = []
        # get frequency dictionary of nums to freq
        # sort dictionary from greatest to smallest freq
        # turn keys into list
        # append first k elements in dictionary to kFinal
        for i in range(len(nums)):
            numFreq[nums[i]] = 1 + numFreq.get(nums[i], 0)
        # print(numFreq)
        numFreq = dict(sorted(numFreq.items(), key=lambda item:item[1], reverse=True))
        # print(numFreq)
        numList = list(numFreq.keys())
        for i in range(k):
            kFinal.append(numList[i])
        return kFinal
            
            