class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSet = set(s)
        tSet = set(t)
        for letter in sSet:
            if (t in tSet):
                return True
        return False