class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]: # Delete at either l or r
                if s[l] == s[r - 1]:
                    r -= 1
                    continue
                if s[l + 1] == s[r]:
                    l += 1
                    continue
                return False
            l += 1
            r -= 1
        return True