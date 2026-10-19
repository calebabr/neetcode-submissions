class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        deletedOne = False
        while l < r:
            if s[l] != s[r]: # Delete at either l or r
                if s[l] == s[r - 1] and not deletedOne:
                    r -= 1
                    deletedOne = True
                    continue
                if s[l + 1] == s[r] and not deletedOne:
                    l += 1
                    deletedOne = True
                    continue
                return False
            else:
                l += 1
                r -= 1
        return True