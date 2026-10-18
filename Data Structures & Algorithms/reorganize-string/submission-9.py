class Solution:
    def reorganizeString(self, s: str) -> str:
        letterFreq = {}
        for char in s:
            letterFreq[char] = -1 + letterFreq.get(char, 0)
        
        maxHeap = []
        for char in letterFreq:
            heapq.heappush(maxHeap, ((letterFreq[char]), char))
        
        # Greedy approach. Pop the letter with higest freq. If we currently have a possible string, check if the char we just popped is equal to the most recent letter we added to the string. If it is and there is no other letter to use in maxHeap, there is no possible arrangement. return "". Else, save this freq and char we just popped, pop the current top and use this top instead and push the freq and char we saved back to the heap. Do this until maxHeap is empty. Return the list res turned into a string.
        res = []
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            if res:
                if char == res[-1]:
                    if not maxHeap:
                        return ""
                    tFreq, tChar = freq, char
                    freq, char = heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, ((tFreq, tChar)))
            res.append(char)
            freq += 1
            if freq == 0:
                continue
            heapq.heappush(maxHeap, (freq, char))
        return ''.join(res)