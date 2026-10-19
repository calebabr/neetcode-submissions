class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = 0
        tp = 0
        while tp < len(t):
            if s[sp] == t[tp] and sp < len(s):
                sp += 1
            if sp >= len(s):
                break
            tp += 1
        if sp == len(s):
            return True
        else:
            return False