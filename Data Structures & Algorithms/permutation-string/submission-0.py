class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Set = set()
        for char in s1:
            s1Set.add(char)
        n = len(s1)
        l = 0
        r = n - 1
        s2Set = set()
        for i in range(n):
            s2Set.add(s2[i])
        if s1Set == s2Set:
            return True
        while r < len(s2) - 1:
            s2Set.remove(s2[l])
            l += 1
            s2Set.add(s2[l])
            r += 1
            s2Set.add(s2[r])
            print(l, r)
            print(s2Set)
            if s1Set == s2Set:
                return True
        return s1Set == s2Set