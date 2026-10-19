class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSet = set(s)
        tSet = set(t)
        for letter in sSet:
            if letter in tSet:
                return True
        return False