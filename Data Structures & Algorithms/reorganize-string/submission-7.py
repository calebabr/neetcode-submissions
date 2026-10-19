class Solution:
    def reorganizeString(self, s: str) -> str:
        letterFreq = {}
        for char in s:
            letterFreq[char] = -1 + letterFreq.get(char, 0)
        
        maxHeap = []
        for char in letterFreq:
            heapq.heappush(maxHeap, ((letterFreq[char]), char))
        
        res = []
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            if res:
                if char == res[-1]:
                    if not maxHeap:
                        return ""
                    tFreq, tChar = heapq.heappop(maxHeap)
                    res.append(tChar)
                    tFreq += 1
                    heapq.heappush(maxHeap, ((tFreq, tChar)))
            res.append(char)
            freq += 1
            if freq == 0:
                continue
            heapq.heappush(maxHeap, (freq, char))
        return ''.join(res)