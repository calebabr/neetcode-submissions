class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # See if permutation of s1 exists as a substring of s2
        # Sliding window + fixed size sliding window
        s1Freq = {}
        s2Freq = {}
        n = len(s1)
        if n > len(s2):
            return False
        # Make first window of size n and check condition
        for i in range(n):
            s1Freq[s1[i]] = 1 + s1Freq.get(s1[i], 0)
        for i in range(n):
            s2Freq[s2[i]] = 1 + s2Freq.get(s2[i], 0)
        if s1Freq == s2Freq:
            return True
        
        # Slide window of size n checking freq at every new window
        l, r = 0, n - 1
        while r < len(s2) - 1:
            s2Freq[s2[l]] -= 1
            if s2Freq[s2[l]] == 0:
                del s2Freq[s2[l]]
            l += 1
            r += 1
            s2Freq[s2[r]] = 1 + s2Freq.get(s2[r], 0)
            if s1Freq == s2Freq:
                return True

        return s1Freq == s2Freq