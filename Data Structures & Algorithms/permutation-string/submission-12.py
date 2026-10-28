class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = {}
        s2Freq = {}
        if len(s1) > len(s2): # IF length of s1 is larger, permutation is impossible so quick exit
            return False
        
        for i in range(len(s1)): # Built first window
            s1Freq[s1[i]] = 1 + s1Freq.get(s1[i], 0)
            s2Freq[s2[i]] = 1+ s2Freq.get(s2[i], 0)
            
        if s1Freq == s2Freq: # early exit if first window true
            return True
        
        l = 0
        r = len(s1) - 1 # slide window of fixed size len(s1) across s2, checking conditon at every iteration
        while r < len(s2) - 1: # len(s2) - 1 because we increment r within the loop
            s2Freq[s2[l]] -= 1
            if s2Freq[s2[l]] == 0:
                del s2Freq[s2[l]]
            l += 1
            r += 1
            s2Freq[s2[r]] = 1 + s2Freq.get(s2[r], 0)
            if s1Freq == s2Freq:
                return True
        # Exit out loop means we've found no equal frequency. return False
        return False