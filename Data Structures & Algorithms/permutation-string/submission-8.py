class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Does a permutation of s1 exist as a substring of s2? permutation = same letters & frequency. Walk through s2 fixed size of s1 checking freq. If ever same, return true. return false after loop
        s1Freq = {}
        s2Freq = {}
        if len(s1) > len(s2):
            return False
        
        # Build for first window
        for i in range(len(s1)):
            s1Freq[s1[i]] = 1 + s1Freq.get(s1[i], 0)
            s2Freq[s2[i]] = 1 + s2Freq.get(s2[i], 0)
        
        if s1Freq == s2Freq:
            return True
        # Walk through s2 and check after building
        l = 0
        r = len(s1) - 1
        while r < len(s2) - 1:
            s2Freq[s2[l]] -= 1
            if s2Freq[s2[l]] == 0:
                del s2Freq[s2[l]]
            l += 1
            r += 1
            s2Freq[s2[r]] = 1 + s2Freq.get(s2[r], 0)
            if s1Freq == s2Freq:
                return True
        return False