class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSet = set(s)
        tSet = set(t)
        for letter in sSet:
            if letter in tSet:
                sSet.remove(letter)
                tSet.remove(letter)
        if (sSet.isEmpty() and tSet.isEmpty()):
            return True
        return False