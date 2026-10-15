class Solution:
    def reorganizeString(self, s: str) -> str:
        freqDict = {}
        for char in s:
            freqDict[char] = 1 + freqDict.get(char, 0) 

        res = []
        freqHeap = []
        # Create a max heap ordered based on freq of (-freq, char)
        for char in freqDict:
            heapq.heappush(freqHeap, ((-1) * freqDict[char], char))
        
        while freqHeap:
            # Greedy approach: Pop the char with the highest freq. If there is something in res, compare with top. If equal and the heap is nonempty, append the next greatest element and push this element back. Return '' if empty because there are no other replacements. Decrement freq each time we use a char in res and if freq is 0, dont push to heap. It cant be used again. Do this while the freq is nonempty.
            freq, char = heapq.heappop(freqHeap)
            freq *= (-1)
            if res:
                if char == res[-1]:
                    if not freqHeap:
                        return ''
                    tempF, tempC = freq, char
                    freq, char = heapq.heappop(freqHeap)
                    freq *= (-1)
                    heapq.heappush(freqHeap, ((-1) * tempF, tempC))
            res.append(char)
            freq -= 1
            if freq == 0:
                continue
            freq *= (-1)
            heapq.heappush(freqHeap, (freq, char))
        return ''.join(res)
