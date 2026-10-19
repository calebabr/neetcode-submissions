class Solution:
    def reorganizeString(self, s: str) -> str:
        letterFreq = {}
        for char in s:
            letterFreq[char] = 1 + letterFreq.get(char, 0)
        
        maxHeap = []
        for char in letterFreq:
            heapq.heappush(maxHeap, (-(letterFreq[char]), char))
        
        res = ''
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            freq *= -1
            freq -= 1
            if res and char == res[-1] and not maxHeap:
                return ""
            
            res = res + char
            if freq == 0:
                continue
            heapq.heappush(maxHeap, (-(freq), char))
        
        return res