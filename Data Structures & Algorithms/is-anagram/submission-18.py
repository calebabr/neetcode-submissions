class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First check if s and t have different lengths, return False if diff
        # create freq dict for each string
        # atp strings have same length, so iterate 0 to lenght s or t
        # at each iteration, add 1 to frequency of the letter at iteration, 0 default
        # return equality check of both freq dicts
        if (len(s) != len(t)):
            return False
        freqS = {}
        freqT = {}
        for i in range(len(s)):
            freqS[s[i]] = 1 + freqS.get(s[i], 0)
            freqT[t[i]] = 1 + freqT.get(t[i], 0)
        return freqS == freqT