class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSet = set(s)
        tSet = set(t)
        sepSet = sSet - tSet
        return (sepSet.length == 0)