class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSet = set(s)
        tSet = set(t)
        sepSet = set()
        for letter in sSet:
            if letter in tSet:
                sepSet.add(letter)
        if (sSet.size() == tSet.size() == sepSet.size()):
            return True
        return False