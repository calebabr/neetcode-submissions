class Solution:
    def reorganizeString(self, s: str) -> str:
        freqDict = {}
        for char in s:
            freqDict[char] = 1 + freqDict.get(char, 0)

        res = ''
        freqHeap = []
        for char in freqDict:
            heapq.heappush(freqHeap, ((-1) * freqDict[char], char))
        
        while freqHeap:
            freq, char = heapq.heappop(freqHeap)
            freq *= (-1)
            if not res:
                res = res + char
            else:
                if char == res[-1]:
                    return ''
                res = res + char
            freq -= 1
            if freq == 0:
                continue
            freq *= (-1)
            heapq.heappush(freqHeap, (freq, char))
        return res
