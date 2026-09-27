class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freqDict = {}
        for i in range(len(arr)):
            freqDict[arr[i]] = 1 + freqDict.get(arr[i], 0)
        freqDict = dict(sorted(freqDict.items(), key=lambda p:p[1], reverse=True))
        for i in freqDict:
            if i == freqDict[i]:
                return i

        return -1